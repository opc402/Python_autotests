import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '697bddd8145ac3a54f9b31ec0290952a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "nuzhnenkov@yandex.ru",
    "password": "Alteza402"
}

body_confirmation = {
    "trainer_token": TOKEN
}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

body_rename = {
    "pokemon_id": "26905",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body_add_pokeball = {
    "pokemon_id": "26905"
}

response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)                              #Создаем переменную = Запрос на регистрацию тренера
print(response.text)                                                                                                           #Вывести тект ответа

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)       #Создаем переменную = Запрос на подтверждение почты
print(response_confirmation.text)                                                                                              #Вывести тект ответа

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)                                 #Создаем переменную = Запрос на создание покемона
print(response_create.text)                                                                                                    #Вывести тект ответа

message = response_create.json()['message']                                                                                    #Создаем переменную = объект message в ответе на запрос на создание покемона
print(message)                                                                                                                 #Вывести message в ответе на запрос на создание покемона

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_rename)                                  #Создаем переменную = Запрос на смену имени покемона
print(response_rename.text)                                                                                                    #Вывести тект ответа

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)        #Создаем переменную = Запрос поймать покемона в покебол
print(response_add_pokeball.text)                                                                                              #Вывести текcт ответа
