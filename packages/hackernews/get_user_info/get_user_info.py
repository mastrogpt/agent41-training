import common 
import requests
from typing import List, Dict

def _get_user_stories(user_name: str, num_stories: str) -> List[Dict]:
    """
    Fetches stories submitted by a specific user.

    Args:
        user_name: Username whose stories to fetch
        num_stories: Number of stories to return (default: 10)

    Returns:
        List[Dict]: List of story dictionaries authored by the user

    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    url = f"{common.BASE_API_URL}/search?tags=author_{user_name},story&hitsPerPage={num_stories}"
    response = requests.get(url)
    response.raise_for_status()
    return [common._format_story_details(story) for story in response.json()["hits"]]

def get_user_info(args):
    user_name = args.get("user_name", "").strip()
    if user_name == "":
        return {"error": "Username is required."}
    num_stories = 10 
    try: num_stories = int(args.get("num_stories", '10'))
    except: pass

    """
    Fetches information about a Hacker News user and their recent submissions.

    Args:
        user_name: Username to fetch information for
        num_stories: Number of user's stories to include (default: 10)

    Returns:
        Dict containing user information and recent stories:
        {
            "id": str,          # Username
            "created_at": str,  # Account creation timestamp
            "karma": int,       # User's karma points
            "about": str,       # User's about text (may be null)
            "stories": list     # List of user's recent story dictionaries
        }

    Raises:
        requests.exceptions.RequestException: If the API request fails
    """
    url = f"{common.BASE_API_URL}/users/{user_name}"
    response = requests.get(url).json()
    response["stories"] = _get_user_stories(user_name, num_stories)
    return response
