import os, requests as req
def test_funcall():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/wheather/funcall"
    res = req.get(url).json()
    assert res.get("output") == "funcall"
