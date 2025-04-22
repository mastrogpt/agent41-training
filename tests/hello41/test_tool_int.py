import os, requests as req
def test_tool():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello41/tool"
    res = req.get(url).json()
    assert res.get("output") == "tool"
