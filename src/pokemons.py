import requests
import src.utils as utils
import src.config as env

def get_count_ata_pokemons () -> int:
  try: 
    response = requests.get(f'{env.API_BASE_URL}/pokemon?limit={env.LIMIT_POKEMONS}')
    
    pokemons = response.json()['results']

    pokemons_filtered = list(filter(utils.check_name, pokemons))

    return len(pokemons_filtered)
    
  except requests.exceptions.RequestException as err:
    raise SystemExit(err)
