import sys
sys.path.append("packages/state/prompt")
import prompt as m

def test_prompt():
    args = {}
    result = m.prompt(args)
    assert result["output"] == ""
    args = {"input": "test input"}
    result = m.prompt(args)
    assert result["output"] == "test input"
