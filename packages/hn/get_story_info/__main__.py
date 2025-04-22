#--kind python:default
#-a mcp:type tool
#-a mcp:desc "Get detailed story info from Hacker News, including the comments"
#-a story_id:str "id of the story to get details for"

import get_story_info
def main(args):
  return get_story_info.get_story_info(args)
