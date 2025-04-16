#--kind python:default
#-a mcp:type resource
#-a mcp:resource "greet://{input}"
#-a mcp:desc "The greeting for a person"
#-a input:str "the input to echo"

import greet
def main(args):
  return greet.greet(args)
