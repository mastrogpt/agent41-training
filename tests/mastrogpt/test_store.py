import sys
sys.path.append("packages/mastrogpt/store")
import store as m

def test_dbquery():
    args = {}
    result = m.store(args)
    assert "output" in result

    args = {"input": "+hello=world"}
    assert result["state"] == "default:30"


