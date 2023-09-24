import requests
import json
import random


POKEAPI_BASE_URL = 'https://pokeapi.co/api/v2/pokemon/'

def get_pokemon_data(name):
    response = requests.get(POKEAPI_BASE_URL + name.lower())
    if response.status_code == 200:
        return response.json()
    else:
        print(f"No data found for Pokemon: {name}")
        return None

def save_to_file(data, filename):
    with open(filename, 'a') as f:
        json.dump(data, f, indent=4)
        f.write('\n')

def get_random_pokemon():
    random_id = random.randint(1, 151)  # limiting to first 151 Pokemons
    response = requests.get(POKEAPI_BASE_URL + str(random_id))
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    pokemons = input("Enter the names of the Pokemons you want to retrieve (comma separated): ").split(',')
    pikachu_included = any(pokemon.lower().strip() == 'pikachu' for pokemon in pokemons)

    print(f"Pikachu included in the list: {pikachu_included}")

    if 'random' in pokemons:
        random_pokemon = get_random_pokemon()
        if random_pokemon:
            print(f"Random Pokemon: {random_pokemon['name']}")
            save_to_file({random_pokemon['name']: random_pokemon['moves']}, 'pokemon_data.txt')

    for pokemon in pokemons:
        pokemon = pokemon.strip()
        if pokemon.lower() == 'random':
            continue
        data = get_pokemon_data(pokemon)
        if data:
            save_to_file({data['name']: data['moves']}, 'pokemon_data.txt')

if __name__ == "__main__":
    main()

