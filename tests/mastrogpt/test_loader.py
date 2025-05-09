import sys
sys.path.append("packages/mastrogpt/loader")
import loader as m

def test_loader():
    args = {}
    result = m.loader(args)
    assert "output" in result
    assert result["state"] == "default:30"
    