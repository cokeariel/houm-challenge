from src.pokemons import get_count_ata_pokemons, get_pokemon_procreators_amount
import src.config as env

print('1) Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. Tu respuesta debe ser un número. \n')

print(f'\t Answer => {get_count_ata_pokemons()} \n')

print('2) ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). Tu respuesta debe ser un número. Recuerda eliminar los duplicados. \n')

print(f'\t Answer => {get_pokemon_procreators_amount(env.NAME_POKEMON_PROCREATOR)} \n')