def greet(args):
  input = args.get("input", "world")
  output = f"Hello, {input}"
  return { "output": output }
