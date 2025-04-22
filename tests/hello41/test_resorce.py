import sys 
sys.path.append("packages/hello41/resorce")
import resorce

def test_resorce():
    res = resorce.resorce({})
    assert res["output"] == "resorce"
