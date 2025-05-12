#--kind python:default
#-a mcp:type tool
#-a mcp:desc "Reverse the input"
#-a input:str "the string to reverse"

import reverse
def main(args):
  return reverse.reverse(args)
