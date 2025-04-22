#--kind python:default
#-a mcp:type prompt
#-a mcp:desc "you are the agent saving the state"
#-a input:str "the user input (default='')"

import role
def main(args):
  return role.role(args)
