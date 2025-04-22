import sys 
sys.path.append("packages/wheather/funcall")
import funcall

def test_funcall():
    res = funcall.funcall({})
    assert res["output"] == "funcall"
