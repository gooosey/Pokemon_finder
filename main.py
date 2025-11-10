import requests
import json
import difflib

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

def get_location(location):
    url = location
    response = requests.get(url)

    if response.status_code == 200:
        location_data = response.json()
        return location_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


# Get all pokemons
def lst_pokemons(lst):
    url = lst
    response = requests.get(url)

    if response.status_code == 200:
        poke_lst = response.json()
        return poke_lst["results"]
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return []
pokemons = [p["name"] for p in lst_pokemons("https://pokeapi.co/api/v2/pokemon?limit=10000")]

# Get custom input
while True:
    pokemon_name = input("What pokemon would you like to inquire about? (type 'Quit' to leave) \n").lower()

    if pokemon_name == "quit":
        break

    if pokemon_name in pokemons:
        print(f"You chose {pokemon_name}")
        break
    else:
        suggestions = difflib.get_close_matches(pokemon_name, pokemons, n=1, cutoff=0.7)
        if suggestions:
            print(f"Did you mean {suggestions}?")
        else:
            print("I don't think that exists")


poke_info = get_pokemon(pokemon_name)
location = get_location(poke_info["location_area_encounters"])

if location:
    area_encounters = [l["location_area"]["name"] for l in location]

if poke_info:
    # Get list of moves
    moves = [move["move"]["name"] for move in poke_info["moves"]]
    
    # Get type of pokemon
    types = [t["type"]["name"] for t in poke_info["types"]]

    # Get stats of pokemon
    stats = {s["stat"]["name"]: s["base_stat"] for s in poke_info["stats"]}
    

    # Format it for json files    
    cleaned = {
        'name' : poke_info["name"],
        'moves': moves,
        'types': types,
        'stats': stats,
        'location': area_encounters
        }

    with open("pokemon_dict.json", "w") as f:
        json.dump(cleaned, f, indent=2)
    
