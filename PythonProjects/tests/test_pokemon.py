import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '779002aa02db9c66c045ddaed7abb558'
HEADER = {'Content-tipe' : 'application/json', 'trainer_token' : TOKEN } 
TRAINER_ID = '25054'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_code():
    response_get = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'