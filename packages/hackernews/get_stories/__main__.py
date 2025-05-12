#--kind python:default
#-a mcp:type tool
#-a mcp:desc "Get stories from Hacker News."
#-a story_type:str "story type (top, new, ask_hn, show_hn) (default='top')" 
#-a num_stories:str "number of stories to fetch (default='10')" 

import get_stories
def main(args):
  return get_stories.get_stories(args)
