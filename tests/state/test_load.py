import sys
sys.path.append("packages/state/load")
import load as m

def test_load():
    args = {}
    result = m.load(args)
    assert result["output"] == ""
    args = {"input": "test input"}
    result = m.load(args)
    assert result["output"] == "test input"
