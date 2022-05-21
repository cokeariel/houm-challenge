import pytest
import json
from src.pokemons import get_pokemon_procreators_amount
from src.utils import check_name, check_pokemon_type_generation

with open('pokemons.json','r') as f:
    pokemons = json.load(f)

# Result can be BOOL
@pytest.mark.parametrize(
    "pokemon",
    [
        (19),
        (200),
        (300),
    ]
)
def test_check_name_bool(pokemon):
    assert type(check_name(pokemons['results'][pokemon])) is bool

# Result has to be TRUE OR FALSE
@pytest.mark.parametrize(
    "pokemon, expected",
    [
        (19, True),
        (200, False),
        (300, False),
    ]
)
def test_check_name_exact(pokemon, expected):
    assert check_name(pokemons['results'][pokemon]) == expected

# Result can be NUMBER
@pytest.mark.parametrize(
    "pokemon",
    [
        (pokemons['results'][200]['name']),
        (pokemons['results'][400]['name']),
        (pokemons['results'][600]['name']),
    ]
)
def test_get_pokemon_procreators(pokemon):
    assert type(get_pokemon_procreators_amount(pokemon)) is int

# Result can be exact NUMBER
@pytest.mark.parametrize(
    "pokemon, expected",
    [
        (pokemons['results'][200]['name'], 116),
        (pokemons['results'][400]['name'], 84),
        (pokemons['results'][600]['name'], 69),
    ]
)
def test_get_pokemon_procreators_exact(pokemon, expected):
    assert get_pokemon_procreators_amount(pokemon) == expected

# Result can be a list, can be empty or with data
@pytest.mark.parametrize(
    "pokemon, max_id",
    [
        ('ice', 2),
        ('poison', 1)
    ]
)
def test_check_pokemon_type_generation(pokemon, max_id):
    assert type(check_pokemon_type_generation(pokemon, max_id)) is list