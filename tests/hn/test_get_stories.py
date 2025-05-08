import sys
sys.path.append("packages/hn/get_stories")
import get_stories as m

def test_get_stories():
    args = { }
    result = m.get_stories(args)
    assert lenr(result["top"]) == 10 
    args = { "story_type": "new", "num_stories": 5 }
    result = m.get_stories(args)
    assert len(result["new"]) == 5 
