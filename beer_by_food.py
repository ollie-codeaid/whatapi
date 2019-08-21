import requests
from pprint import pprint

response = requests.get("https://api.punkapi.com/v2/beers?per_page=80")

beers = response.json()

beer_by_food = {}

for beer in beers:
    for food in beer["food_pairing"]:
        beer_for_food = beer_by_food.get(food, [])
        beer_for_food.append(beer["name"])
        beer_by_food[food] = beer_for_food

pprint(beer_by_food)
