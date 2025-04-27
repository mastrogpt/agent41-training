#--kind python:default
#-a mcp:type prompt
#-a mcp:desc "Which person you are."
#-a person:str "who you are impersonating (default='a helpful assistant.')"
import person

def main(args):
  return person.person(args) 
