import sys
sys.path.append("packages/mastrogpt/sql")
import sql as m

def test_dbquery():
    args = {}
    result = m.sql(args)
    assert "error" in result

    sql = "create table test (id int, name varchar(255))"
    args = {"input": sql}
    result = m.sql(args)
    assert "create" in result

    sql = "insert into test(id, name) values(1, 'Mike')"
    args = {"input": sql}
    result = m.sql(args)
    assert result["insert"] == "affected rows: 1"

    args = {"input": "insert into test(id, name) values(2, 'Miri')", "__ow_method": "GET"}
    result = m.sql(args)
    assert result["output"] == "insert: affected rows: 1"

    args = {"input": "insert into test(id, name) values(3, 'Max')\n insert into test(id, name) values(3, 'Aur')"}
    result = m.sql(args)
    assert "multiple" in result

    sql =  "select * from test"
    args = {"input": sql}
    result = m.sql(args)
    assert len(result["select"]) == 4

    sql =  "select * from test"
    args = {"input": sql, "__ow_method": "GET"}
    result = m.sql(args)
    assert result["output"] == "found 4 rows"
    assert "html" in result

    sql =  "drop table test"
    args = {"input": sql, "__ow_method": "GET"}    
    result = m.sql(args)
    assert result["output"] == "drop: affected rows: -1"

    