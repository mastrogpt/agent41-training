import sys
sys.path.append("packages/hn/search_stories")
import search_stories as m

def test_search_stories():
    args = { }
    result = m.search_stories(args)
    assert result["error"] == "Query string is required."
    args = { "query": "python", "num_results": 5, "search_by_date": True }
    result = m.search_stories(args)
    assert len(result["found_stories"]) == 5
