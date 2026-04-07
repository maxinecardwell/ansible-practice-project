import requests

# Base URL used for all API requests to avoid repetition
base_url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(base_url)
pokemon_data = response.json()
