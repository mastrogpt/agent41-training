import sys 
sys.path.append("packages/hello41/tool")
import tool

def test_tool():
    res = tool.tool({})
    assert res["output"] == "tool"
