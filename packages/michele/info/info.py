import os
def info(args):
  input = args.get("input", "")
  output = "Please specify the input, valid inputs are: name, age, city"
  if input.find("name") != -1: 
    output = "name: Michele Sciabarra"
  elif input.find("age") != -1:
    output = "age: 56"
  elif input.find("city") != -1:
    output = "city: Lodon"

  return { "output": output }
