import sys
sys.path.append("packages/state/save")
import save as m

def test_save():
    args = {}
    result = m.save(args)
    assert result["output"] == ""
    args = {"input": "test input"}
    result = m.save(args)
    assert result["output"] == "test input"
