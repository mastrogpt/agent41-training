import common
import requests

def get_stories(args):
  #print(args)
  story_type = args.get("story_type", "top").lower().strip()
  num_stories = 10 
  try: num_stories = int(args.get("num_stories"))
  except: pass

  output = {"error": "bad parameters"}

  params = common.api_params.get(story_type)
  if params: 
    url = f"{common.BASE_API_URL}/{params['endpoint']}?tags={params['tags']}&hitsPerPage={num_stories}"
    response = requests.get(url)
    if response.status_code == 200:
      hits = response.json()["hits"]
      output = [common._format_story_details(story) for story in hits]

  #print(output)
  return {story_type: output }

