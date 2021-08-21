import requests
d = {}
r = requests.get("https://api.teleport.org/api/cities/")
for i in r.json()['_embedded']['city:search-results']:
    print(i)