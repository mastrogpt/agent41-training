import sys
sys.path.append("packages/hn/get_user_info")
import get_user_info as m

def test_get_user_info():
    args = { }
    result = m.get_user_info(args)
    assert  "error" in result
    args = { "user_name": "msciabarra", "num_stories": 5 }
    result = m.get_user_info(args)
    assert result["username"] == "msciabarra"
    assert len(result["stories"]) == 5
