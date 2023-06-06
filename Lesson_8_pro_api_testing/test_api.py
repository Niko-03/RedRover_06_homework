import requests                                                 # импорты для работы с api
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'        # в переменной сохранили ссылку на сайт, с которым будем работать
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'           # для авторизации
STATUS_OK = 200


@pytest.fixture(scope='module')                   # создали фикстуру для авторизации, результат сможем применить во всех остальных наших тестовых методах
def auth_token():                                 # scope='module' означает, что фикстура применима ко всему нашему файлу
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)                 # response - это объект (переменная)
    response_data = response.json()
    token = response_data['token']                                   # в переменную сохранили значение токена
    assert response.status_code == STATUS_OK
    yield token                                                      # вернули токен


@pytest.fixture(scope='module')                                       # фикстура для сохранения booking_id
def booking_id():
    payload = {
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)               # .post - загрузка данных в систему    (или (data=payload)....)
    booking_id = response.json()['bookingid']                      # в переменной сохранили значение id от 'bookingid'
    assert response.status_code == 200
    yield booking_id




# ------------------- метод GET ---------------------------------------------------------------

def test_get_all_bookings():                               # получить информация о всех бронированиях (get)
    response = requests.get(BASE_URL)                      # в переменной response сохраним ответ, который вернётся на наш get-запрос
    print(f'\n{len(response.json())}')                     # посмотреть длину (количество ключей)
    # print(response.status_code)                          # распечатаем статус-код (200, например)
    assert response.status_code == STATUS_OK               #

    # print(f'\n{response.headers}')                        # все наши хедеры, соединения, контент json, кодировка, дата....
    # print(response.json())                                #

    # headers = ('Connection', 'keep-alive')                # пару ключ:значение проверяем через items()
    # assert headers in response.headers.items()            #

    key = 'Connection'                                      # если проверяем только ключ, то так (всё по правилам работы со словарями)
    assert key in response.headers                          #


def test_get_booking_with_id():                             # тест по id - инфа по одному бронированию с id = 1
    response = requests.get(f'{BASE_URL}/1')                # к нашему URL добавили ID (через /, т.е. "/1" - это id)
    response_data = response.json()                         # здесь сохраним наш ответ в формате json
    expected_keys = ['firstname', 'lastname', 'totalprice', 'depositpaid', 'bookingdates']
    # assert response_data['firstname'] == 'Eric'            # из-за этого assert`а тест может падать, т.к. данные динамично меняются
    for key in expected_keys:
        assert key in response_data.keys()
    print(f'\n{response_data}')                              # распечатаем ответ



# ------------------- метод POST (перенесли в фикстуру для booking_id)---------------------------------------------------------------

# def test_create_booking():                                   # post    --->> перенесли в фикстуру для сохранения booking_id
#     payload = {                                              # загружаемые данные (обычно переменную называют payload)
#             "firstname": "John",
#             "lastname": "Smith",
#             "totalprice": 111,
#             "depositpaid": True,
#             "bookingdates": {
#                 "checkin": "2018-01-01",
#                 "checkout": "2019-01-01"
#             },
#             "additionalneeds": "Breakfast"
#     }
#     response = requests.post(BASE_URL, json=payload)         # .post - загрузка данных в систему    (или (data=payload)....)
#     # print(response.json())                                # посмотрим на id, который был сгенерирован, чтобы проверить, что запись создана (по какому ключу нам обратиться, чтобы увидеть id)
#     booking_id = response.json()['bookingid']               # в переменной сохранили значение id от 'bookingid'
#     assert response.status_code == 200
#     response_get = requests.get(f'{BASE_URL}/{booking_id}')        # переменная - обратимся к энд-поинту с конкретным id, чтобы проверить, что запись создана (или чтобы обратиться к ней позже)
#     assert response_get.status_code == 200                         # при помощи .get посмотрим на нашу запись в booking_id (???)
#     assert payload['firstname'] in response_get.json().values()    # проверяем, что в сгенерированной записи есть 'firstname' с определённым значением
                                                                   # test_api.py::test_create_booking PASSED - значит наша запись добавилась


# ------------------------- метод POST с фикстурой ------------------------------------------


def test_create_booking(booking_id):
    response = requests.get(
    f'{BASE_URL}/{booking_id}')
    assert response.status_code == 200
    assert response.json()['firstname'] == 'John'



''' Ограничение метода .post в том, что доступ к переменной booking_id мы можем видеть только внутри этой функции, например.
    Но можно вынести создание метода .post в фикстуру, сделать доступ к ней на уровне сессии, 
    и в этом случае полученный id (например) будет виден во всех наших методах.
'''

''' CRUD - все эти операции можно выполнить внутри одного тестового метода
Create — создание
Read — чтение
Update — обновление
Delete — удаление
'''

# -------------------- авторизация (Auth - CreateToken) - перенесено в фикстуру -------------------


def test_user_autorization():
    payload = {
            "username": "admin",
            "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)                 # response - это объект (переменная)
    response_date = response.json()
    # print(response.json())                                         # в результате теста вернулся токен  {'token': 'ecddd747ece3dab'}
    assert response.status_code == STATUS_OK
    assert 'token' in response_date




# ------------------- метод PUT - внести изменения ---------------------------------------------------------------


def test_update_booking(booking_id, auth_token):       # для удаления данных используется токен, для этого передаём обе фикстуры как параметры функции)
    payload = {                                        # при изменении каких-то данных берём все данные переменной pyload (весь pyload должен быть передан)
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 500,                            # вносим необходимые изменения
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Lunch"                     # вносим необходимые изменения
    }
    headers = {'Cookie': f'token={auth_token}'}

    response = requests.put(f'{BASE_URL}/{booking_id}', json=payload, headers=headers)          # обращаемся к нашим энд-поинт методом .put
    assert response.status_code == 200

    response_get = requests.get(f'{BASE_URL}/{booking_id}')                                    # проверка
    response_data = response_get.json()
    assert response.status_code == 200
    assert response_data['totalprice'] == payload['totalprice']
    assert response_data['additionalneeds'] == payload['additionalneeds']




# ------------------- метод DELETE - удалить запись ---------------------------------------------------------------


def test_delete_booking(booking_id, auth_token):
    headers = {'Cookie': f'token={auth_token}'}
    response = requests.delete(f'{BASE_URL}/{booking_id}', headers=headers)
    assert response.status_code == 201

    response_get = requests.get(f'{BASE_URL}/{booking_id}')                              # проверка
    assert response_get.status_code == 404







