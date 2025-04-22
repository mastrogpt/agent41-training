import os, requests as req
def test_prompt():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/hello41/prompt"
    res = req.get(url).json()
    assert res.get("output") == "prompt"
