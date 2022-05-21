import requests
import src.config as env
from typing import List

def check_name (pokemon) -> bool:
  """
  Check if name contains "at" and another "a"
  -> return: a boolean, equivalent to if name contains "at" and another "a"
  """
  name = pokemon['name']
  if 'at'in name and name.count('a') == 2:
    return True
  else:
    return False

def check_pokemon_type_generation (type: str, id_max_pokemon: int):
    """
    Check if pokemons by type, is greater than id limit (id_max_pokemon)
    -> return: a list with objects, each object has an id and name
    """
    response = requests.get(f'{env.API_BASE_URL}/type/{type}')
    pokemons = response.json()['pokemon']

    output = []
    for pokemon in pokemons:
      response = requests.get(pokemon['pokemon']['url'])

      if response.json()['id'] > id_max_pokemon: continue
      output.append({ "id": response.json()["id"], "weight": response.json()["weight"] })

    return output
