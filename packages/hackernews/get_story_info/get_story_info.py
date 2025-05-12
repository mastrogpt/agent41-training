import common
def get_story_info(args):
    """
    Fetches detailed information about a specific story including comments.

    Args:
        story_id: The ID of the story to fetch

    Returns:
        Dict containing full story details:
        {
            "id": int,          # Story ID
            "title": str,       # Story title
            "url": str,         # Story URL (may be null for text posts)
            "author": str,      # Author username
            "points": int,      # Points (may be null)
            "comments": list    # Nested list of comment dictionaries
        }

    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    try: 
       story_id = int(args.get("story_id"))
    except:
        return {"error": "Story ID is required."}
    story = common._get_story_info(story_id)
    details = common._format_story_details(story, basic=False)
    return {
        "story": details
    }

