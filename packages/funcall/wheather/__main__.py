#--kind python:default
#-a mcp:type tool
#-a mcp:desc "wheather forecast"
#-a location:str "location of the foreacast"

import wheather
def main(args):
  return wheather.wheather(args)
