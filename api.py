import urllib.request
import json

url = "https://api.github.com/search/code?q=addClass+in:file+language:js+repo:jquery/jquery"
json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)

for item in data['items']:
    print (item['name'])
    print(item['path'])


def github_search(jquery):
    url = "https://api.github.com/search/?"