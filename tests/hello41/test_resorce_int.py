import os, requests as req
def test_resorce():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello41/resorce"
    res = req.get(url).json()
    assert res.get("output") == "resorce"
