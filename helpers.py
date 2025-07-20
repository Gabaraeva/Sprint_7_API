import requests
import random
import string


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier',
        data=payload
    )

    if response.status_code == 201:
        return {
            "login": login,
            "password": password,
            "first_name": first_name,
            "response": response
        }
    return {"response": response}


def login_courier(login, password):
    return requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
        data={"login": login, "password": password}
    )


def delete_courier(courier_id):
    return requests.delete(
        f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}'
    )


def create_order(color=None):
    payload = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, Кремль, 1",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2025-07-20",
        "comment": "Комментарий",
    }
    if color:
        payload["color"] = color
    return requests.post(
        'https://qa-scooter.praktikum-services.ru/api/v1/orders',
        json=payload
    )


def get_orders_list():
    return requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')



