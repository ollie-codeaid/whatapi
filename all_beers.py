import requests
from pprint import pprint

response = requests.get("https://api.punkapi.com/v2/beers?per_page=1000")

pprint(response.json())
