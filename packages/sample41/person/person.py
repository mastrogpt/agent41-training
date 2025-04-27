def person(args):
  input = args.get("person", "a helpful assistant.")
  output = f"You are {input}"
  return { "output": output }
