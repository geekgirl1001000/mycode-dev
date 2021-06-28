import requests
import json

# get, post, put, delete, patch

url="https://opentdb.com/api.php?amount=3&category=27&difficulty=medium&type=multiple"

resp = requests.get(url)

print(dir(resp))

x=resp.json()

print (x)
print(type(x))

#print(x["results"][0]["question"])

#dump a json object into your pythin string
json.loads(x)

print(x)

