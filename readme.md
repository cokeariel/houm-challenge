# HOUM-CHALLENGE

## PokeAPI-Challenge

1.- Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. Tu respuesta debe ser un número.

2.- ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). Tu respuesta debe ser un número. Recuerda eliminar los duplicados.

3.- Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.


## Instalación

Codigo probado en Python 3.9.12

Previo a ejecución, se necesita clonar repositorio e instalar requirements.txt 
```
git clone
pip3 install -r requirements.txt
```

## Ejecución
Generar Respuesta a preguntas 1, 2 y 3
Ejecutar:
```
python3 main.py
```

Generar Test
Ejecutar:
```
pytest test_main.py -v
```
o
Ejecutar:
```
python3 -m pytest test_main.py -v
```