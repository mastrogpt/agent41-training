import sys
sys.path.append("packages/hn/get_story_info")
import get_story_info as m

def test_get_story_info():
    args = { }
    result = m.get_story_info(args)
    assert "error" in result 
    args = { "story_id": 12345 }
    result = m.get_story_info(args)
    assert "story" in result
