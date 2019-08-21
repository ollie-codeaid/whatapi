import requests
from pprint import pprint

response = requests.get("https://api.punkapi.com/v2/beers?per_page=80")

pprint(response.json())
