import requests

def wheather(args):

  location = args.get("location", "")
  forecast = "Please provide a location."

  location = "Rome"

  res = requests.get(f"https://wttr.in/{location}?format=3")
  res.text
  
  
  return { "forecast": forecast }
