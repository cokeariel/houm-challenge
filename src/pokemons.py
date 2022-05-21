import requests
import src.utils as utils
import src.config as env
from typing import List

def get_count_ata_pokemons () -> int:
  """
  Obtains the number of Pokemons with "at" and another "a"
  -> return: a number, equivalent a number of Pokemons with "at" and another "a"
  """
  try:
    response = requests.get(f'{env.API_BASE_URL}/pokemon?limit={env.LIMIT_POKEMONS}')

    pokemons = response.json()['results']

    pokemons_filtered = list(filter(utils.check_name, pokemons))

    return len(pokemons_filtered)

  except requests.exceptions.RequestException as err:
    raise SystemExit(err)

def get_pokemon_procreators_amount (pokemon_name: str) -> int:
  """
  Obtains the number of Pokemons to can procreate
  -> param name: the name of a Pokemon, it must be typeof string
  -> return: a number, equivalent a number of Pokemons to can procreate
  """
  try:
    response = requests.get(f'{env.API_BASE_URL}/pokemon-species/{pokemon_name}')

    specie = response.json()

    names = set()
    for egg_group in specie['egg_groups']:
      response = requests.get(egg_group['url'])

      pokemon_species = response.json()['pokemon_species']

      for pokemon_specie in pokemon_species:
        names.add(pokemon_specie['name'])

    return len(names)

  except requests.exceptions.RequestException as err:
    raise SystemExit(err)

def get_weights_by_pokemon_type (pokemon_type: str) -> List[int]:
  """
  Obtains according to Pokemon type, the maximum and minimum weight
  -> param pokemon_type: the pokemon type, it must be typeof string
  -> return: a list of [max_weight: int, min_weight: int]
  """
  try:
    pokemons = utils.check_pokemon_type_generation(pokemon_type, env.LIMIT_ID_FIRST_GENERATION)

    max_weight = 0
    min_weight = 99999999
    for pokemon in pokemons:
      if pokemon['weight'] > max_weight:
        max_weight = pokemon['weight']

      if pokemon['weight'] < min_weight:
          min_weight = pokemon['weight']

    return [max_weight, min_weight]

  except requests.exceptions.RequestException as err:
    raise SystemExit(err)