#--kind python:default
#--web true
#--param OLLAMA_HOST "localhost"
#--param AUTHOR $AUTH

import forecast
def main(args):
  return { "body": forecast.forecast(args) }
