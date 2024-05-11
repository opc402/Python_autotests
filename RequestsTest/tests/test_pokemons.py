import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = '697bddd8145ac3a54f9b31ec0290952a'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '2809'

def test_status_code():                                                                                             #Тест на статус код 200
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})                          #Ответ = Запрос на получение списка покемонов
    assert response.status_code == 200                                                                              #Проверка, что статус ответа равен 200

def test_part_of_response():                                                                                        #Тест на текст в ответе
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})                      #Ответ = Запрос на получение списка покемонов
    assert response_get.json()["data"][0]["name"] == 'Бульбазавр'                                                   #Проверка, что в ответе приходит имя Бульбазавр

@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '26908')])       #Создаем фикстуру или предварительнаю функцию, которая имеет слудующий вид ('ключ, значение', [(), (), ()])
def test_parametrize(key, value):                                                                                   #Тест, для которого мы берем указанные выше ключи и значения
    response_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})              #Ответ = Запрос на получение списка покемонов
    assert response_parametrize.json()["data"][0][key] == value                                                     #Проверка, что в ответе на запрос за списком покемонов, ключ равен значению указаному выше

def test_status_code_trainers():                                                                                    #Тест на статус код 200
    response_get_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})             #Ответ = Запрос на получение списка тренеров
    assert response_get_trainers.status_code == 200                                                                 #Проверка, что статус ответа равен 200

def test_trainer_id():                                                                                              #Тест id тренера
    response_get_trainers = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})             #Ответ = Запрос на получение списка тренеров
    assert response_get_trainers.json()["data"][0]["id"] == TRAINER_ID                                              #Проверка, что в ответе есть тренер с нашим id
