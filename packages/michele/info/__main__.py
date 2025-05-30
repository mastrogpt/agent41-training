#--kind python:default
#--web true
#-a mcp:type tool
#-a mcp:desc "Provide informations about Michele"
#-a input:str "input=name to get the name, input=age to get the age, input=city to get the city (default='')"
#-p REDIS_URL "$REDIS_URL"
#-p REDIS_PREFIX "$REDIS_PREFIX"

import info

def main(args):
  # invoked as web action
  if "__ow_method" in args:
    import os, redis
    [user, secret] = args.get("token", "_:_").split(":")
    rd = redis.from_url(args.get("REDIS_URL"))
    check = rd.get(f"{args.get("REDIS_PREFIX")}TOKEN:{user}") or b''
    if check.decode('utf-8') == secret:
        return {"body": info.info(args)}
    return {"body": "unauthorized"}
  # CLI access
  return info.info(args)
