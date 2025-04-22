#--kind python:default
#-a mcp:type tool
#-a mcp:desc "save the state"
#-a input:str "the user input (default='')"

import save
def main(args):
  return save.save(args)
