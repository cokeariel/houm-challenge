from src.pokemons import get_count_ata_pokemons, get_pokemon_procreators_amount, get_weights_by_pokemon_type
import src.config as env

print('============================================================')

print('1) Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. Tu respuesta debe ser un número. \n')

print(f'\t Answer => {get_count_ata_pokemons()} \n')

print('============================================================')

print('2) ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). Tu respuesta debe ser un número. Recuerda eliminar los duplicados. \n')

print(f'\t Answer => {get_pokemon_procreators_amount(env.NAME_POKEMON_PROCREATOR)} \n')

print('============================================================')

print('3) Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo. \n')

print(f'\t Answer => {get_weights_by_pokemon_type(env.TYPE_POKEMON_FIRST_GENERATION)} \n')

print('============================================================')