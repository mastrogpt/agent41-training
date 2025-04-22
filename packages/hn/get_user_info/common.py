import requests

from typing import List, Dict, Union, Any

BASE_API_URL = "http://hn.algolia.com/api/v1"
DEFAULT_NUM_COMMENTS = 10
DEFAULT_COMMENT_DEPTH = 2

api_params = {
      "top": {"endpoint": "search", "tags": "front_page"},
      "new": {"endpoint": "search_by_date", "tags": "story"},
      "ask_hn": {"endpoint": "search", "tags": "ask_hn"},
      "show_hn": {"endpoint": "search", "tags": "show_hn"}
}

def _get_story_info(story_id: int) -> Dict:
    """
    Fetches detailed information about a Hacker News story.

    Args:
        story_id: The ID of the story to fetch

    Returns:
        Dict: Raw story data from the HN API including title, author, points, url and comments

    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    url = f"{BASE_API_URL}/items/{story_id}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def _format_story_details(story: Union[Dict, int], basic: bool = True) -> Dict:
    """
    Formats a story's details into a standardized dictionary structure.

    Args:
        story: Either a story ID or dictionary containing story data
        basic: If True, excludes comments. If False, includes formatted comments to depth of 2

    Returns:
        Dict with the following structure:
        {
            "id": int,          # Story ID
            "title": str,       # Story title if present
            "url": str,         # Story URL if present
            "author": str,      # Author username
            "points": int,      # Points (may be null)
            "comments": list    # List of comment dicts (only if basic=False)
        }

    The function handles both raw story IDs and story dictionaries, fetching additional
    data if needed. For non-basic requests, it ensures comments are properly formatted.
    """
    if isinstance(story, int):
        story = _get_story_info(story)
    output = {
        "id": story["story_id"],
        "author": story["author"],
    }
    if "title" in story:
        output["title"] = story["title"]
    if "points" in story:
        output["points"] = story["points"]
    if "url" in story:
        output["url"] = story["url"]
    if not basic:
        if _validate_comments_is_list_of_dicts(story["children"]):
            story = _get_story_info(story["story_id"])
        output["comments"] = [
            _format_comment_details(child) for child in story["children"]
        ]
    return output

def _validate_comments_is_list_of_dicts(comments: List[Any]) -> bool:
    """
    Validates if the comments list contains dictionaries or just IDs.

    Args:
        comments: List of comments to validate

    Returns:
        bool: False if comments contains IDs that need to be fetched, True if comments are already dictionaries

    This is used to determine if we need to fetch the full story info to get comment details.
    """

def _format_comment_details(comment: Dict, depth: int = DEFAULT_COMMENT_DEPTH, num_comments: int = DEFAULT_NUM_COMMENTS) -> Dict:
    """
    Formats a comment and its replies into a standardized structure.

    Args:
        comment: Raw comment dictionary from the API
        depth: How many levels of nested comments to include (default: 2)
        num_comments: Maximum number of child comments to include per level (default: 10)

    Returns:
        Dict with the following structure:
        {
            "author": str,      # Comment author's username
            "text": str,        # Comment text content
            "comments": list    # List of nested comment dicts (only if depth > 1)
        }

    The function recursively formats nested comments up to the specified depth,
    limiting the number of child comments at each level to num_comments.
    """
    output = {
        "author": comment["author"],
        "text": comment["text"],
    }
    if depth > 1 and len(comment["children"]) > 0:
        output["comments"] = [
            _format_comment_details(child, depth - 1, num_comments) for child in comment["children"][:num_comments]
        ]
    return output


