import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '779002aa02db9c66c045ddaed7abb558'
HEADER = {'Content-tipe' : 'application/json', 'trainer_token' : TOKEN }

body_create = {
    
    "name": "Бульбазавр",
    "photo_id": 1

}

body_change = {
    "pokemon_id": "184639",
    "name": "Ksu",
    "photo_id": 1
}

body_pokeball = {
     "pokemon_id": "184639"
}

body_trainer_name = {
    "name": "Бульбазавр",
    "city": "москва"
}
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''

response_trainer_name = requests.put(url = f'{URL}/trainers', headers = HEADER, json = body_trainer_name)
print(response_trainer_name.text)
