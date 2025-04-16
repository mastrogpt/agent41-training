def person(args):
  input = args.get("input", "a nice person")
  output = f"You are {input}"
  return { "output": output }
