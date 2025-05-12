import common
import requests

def search_stories(args):
    """
      Searches Hacker News stories using a query string.

      Args:
          query: Search terms to find in stories
          num_results: Number of results to return (default: 10)
          search_by_date: If True, sorts by date. If False, sorts by relevance/points/comments (default: False)

      Returns:
          List[Dict]: List of matching story dictionaries, each containing:
          {
              "id": int,          # Story ID
              "title": str,       # Story title
              "url": str,         # Story URL
              "author": str,      # Author username
              "points": int,      # Points (may be null)
          }

      Raises:
          requests.exceptions.RequestException: If the API request fails
    """
    search_by_date = args.get("search_by_date", False)
    num_results = 10
    try: num_results = int(args.get("num_results", 10))
    except: pass
    query = args.get("query")
    if not query:
        return {"error": "Query string is required."}
    if search_by_date:
        url = f"{common.BASE_API_URL}/search_by_date?query={query}&hitsPerPage={num_results}&tags=story"
    else:
        url = f"{common.BASE_API_URL}/search?query={query}&hitsPerPage={num_results}&tags=story"
    print(url)
    response = requests.get(url)
    response.raise_for_status()
    found = [common._format_story_details(story) for story in response.json()["hits"]]  
    return { "found_stories": found }
