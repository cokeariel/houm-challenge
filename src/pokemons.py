import requests

base_url = 'https://pokeapi.co/api/v2'
limit_pokemons = 1126

def check_name (pokemon):
  name = pokemon['name']
  if 'at'in name and name.count('a') == 2:
    return True
  else:
    return False

def get_count_ata_pokemons () -> int:
  try: 
    response = requests.get(f'{base_url}/pokemon?limit={limit_pokemons}')
    
    pokemons = response.json()['results']

    pokemons_filtered = list(filter(check_name, pokemons))

    return len(pokemons_filtered)
    
  except requests.exceptions.RequestException as err:
    raise SystemExit(err)
