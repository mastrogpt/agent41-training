#--kind python:default
#-a mcp:type resource
#-a mcp:resource "greet://{input}"
#-a mcp:desc "The greeting for a person"
#-a greet:str "the greeting to use (default='Hello')"

import greet
def main(args):
  return greet.greet(args)
