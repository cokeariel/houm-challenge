# HOUM-CHALLENGE

## PokeAPI-Challenge

1.- Obtén cuantos pokemones poseen en sus nombres “at” y tienen 2 “a” en su nombre, incluyendo la primera del “at”. Tu respuesta debe ser un número.

2.- ¿Con cuántas especies de pokémon puede procrear raichu? (2 Pokémon pueden procrear si están dentro del mismo egg group). Tu respuesta debe ser un número. Recuerda eliminar los duplicados.

3.- Entrega el máximo y mínimo peso de los pokémon de tipo fighting de primera generación (cuyo id sea menor o igual a 151). Tu respuesta debe ser una lista con el siguiente formato: [1234, 12], en donde 1234 corresponde al máximo peso y 12 al mínimo.

## Instalación

> Programa ejecutado en Python ^3.9.12

Clonar repositorio:
```
git clone https://github.com/cokeariel/houm-challenge.git
```
Para la instalación de las dependencias, ejecturar el siguiente comando:
```
pip3 install -r requirements.txt
```

## Ejecución 

Para obtener las respuestas a las preguntas 1,2 y 3 del desafío, ejecutar el siguiente comando:
```
python main.py
```

## Testing

Para ejecutar los test de este programa, ejecutar el siguiente comando:
```
python -m pytest test_main.py -v
```