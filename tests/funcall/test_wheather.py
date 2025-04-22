import sys 
sys.path.append("packages/funcall/wheather")
import wheather

def test_wheather():
    res = wheather.wheather({})
    assert res["output"] == "wheather"
