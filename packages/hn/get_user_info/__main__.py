#--kind python:default
#-a mcp:type tool
#-a mcp:desc "Get user info from Hacker News,"
#-a num_stories:str "number of stories to return (default='10')"
#-a user_name:str "usernme to get info for"

import get_user_info
def main(args):
  return get_user_info.get_user_info(args)
