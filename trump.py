import requests

TRUMP_URL = "https://api.tronalddump.io/random/quote"

trump_response = requests.get(TRUMP_URL)
trump_quote = trump_response.json()["value"]

print (trump_quote)
