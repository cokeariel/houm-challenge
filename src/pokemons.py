import requests
import src.utils as utils
import src.config as env
from typing import List

def get_count_ata_pokemons () -> int:
  try:
    response = requests.get(f'{env.API_BASE_URL}/pokemon?limit={env.LIMIT_POKEMONS}')

    pokemons = response.json()['results']

    pokemons_filtered = list(filter(utils.check_name, pokemons))

    return len(pokemons_filtered)

  except requests.exceptions.RequestException as err:
    raise SystemExit(err)

def get_pokemon_procreators_amount (pokemonName: str) -> int:
  try:
    response = requests.get(f'{env.API_BASE_URL}/pokemon-species/{pokemonName}')

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

def get_weights_by_pokemon_type (pokemonType: str) -> List[int]:
  try:
    response = requests.get(f'{env.API_BASE_URL}/type/{pokemonType}')
    pokemonsType = response.json()['pokemon']

    max_weight = 0
    min_weight = 99999999
    for pokemonType in pokemonsType:
      response = requests.get(pokemonType['pokemon']['url'])
      pokemon = response.json()

      if pokemon['id'] > env.LIMIT_ID_FIRST_GENERATION: continue

      if pokemon['weight'] > max_weight:
        max_weight = pokemon['weight']

      if pokemon['weight'] < min_weight:
          min_weight = pokemon['weight']

    return [max_weight, min_weight]

  except requests.exceptions.RequestException as err:
    raise SystemExit(err)