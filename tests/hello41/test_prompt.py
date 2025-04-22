import sys 
sys.path.append("packages/hello41/prompt")
import prompt

def test_prompt():
    res = prompt.prompt({})
    assert res["output"] == "prompt"
