#--kind python:default
#-a mcp:type resource
#-a mcp:desc "read the state"
#-a input:str "the user input (default='')"

import load
def main(args):
  return load.load(args)
