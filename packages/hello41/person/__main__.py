#--kind python:default
#-a mcp:type prompt
#-a mcp:desc "Which person you are."
#-a input:str "which person you are"
import person

def main(args):
  return person.person(args) 
