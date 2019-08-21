import requests
from pprint import pprint

response = requests.get("https://api.punkapi.com/v2/beers?per_page=80")

beers = response.json()

beer_by_contributor = {}

for beer in beers:
    contributed_by = beer["contributed_by"]
    contributor_beers = beer_by_contributor.get(contributed_by, [])
    contributor_beers.append(beer["name"])
    beer_by_contributor[contributed_by] = contributor_beers

pprint(beer_by_contributor)
