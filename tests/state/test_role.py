import sys
sys.path.append("packages/state/role")
import role as m

def test_role():
    args = {}
    result = m.role(args)
    assert result["output"] == ""
    args = {"input": "test input"}
    result = m.role(args)
    assert result["output"] == "test input"
