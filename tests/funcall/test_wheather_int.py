import os, requests as req
def test_wheather():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/funcall/wheather"
    res = req.get(url).json()
    assert res.get("output") == "wheather"
