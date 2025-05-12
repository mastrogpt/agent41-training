#--kind python:default
#-a mcp:type tool
#-a mcp:desc "Search stories from Hacker News."
#-a num_results:str "number of results to return (default=10)"
#-a search_by_date:bool "if True, sorts by date. If False, sorts by relevance/points/comments (default=False)"
#-a query:str "search terms to find in stories"

import search_stories
def main(args):
  return search_stories.search_stories(args)
