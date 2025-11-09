import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        poke_data = response.json()
        return poke_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = 'ditto'
poke_info = get_pokemon(pokemon_name)


if poke_info:
    print(poke_info["name"])