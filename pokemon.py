#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokenum}").json()

    #print(pokeapi["sprites"]["front_default"])

    #moves = pokeapi["moves"]
    for i in pokeapi["moves"]:
        print(i["move"]["name"])

main()
