import requests
from dotenv import load_dotenv
from os import getenv
from urllib.parse import quote
from uuid import uuid4

load_dotenv()

API_KEY = getenv("VOICE_RSS_API_KEY")
TTS_BASE_URL = f"http://api.voicerss.org/?key={API_KEY}&hl=en-us&src="
TRUMP_URL = "https://api.tronalddump.io/random/quote"

trump_response = requests.get(TRUMP_URL)
trump_quote = trump_response.json()["value"]

encoded_quote = quote(trump_quote)

text_response = requests.get(TTS_BASE_URL + encoded_quote)

file_name = f"wav_output/{uuid4()}.wav"
with open(file_name, "bx") as f:
  f.write(text_response.content)

print(file_name)
