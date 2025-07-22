import requests
import random
import string
import allure
from urls import Urls


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


@allure.step("Регистрация нового курьера")
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
        Urls.CREATE_COURIER,
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


@allure.step("Авторизация курьера")
def login_courier(login, password):
    return requests.post(
        Urls.LOGIN_COURIER,
        data={"login": login, "password": password}
    )


@allure.step("Удаление курьера")
def delete_courier(courier_id):
    return requests.delete(
        f"{Urls.DELETE_COURIER}{courier_id}"
    )


@allure.step("Создание заказа")
def create_order(color=None):
    from data import TestData
    payload = TestData.ORDER_DATA.copy()

    if color:
        payload["color"] = color
    return requests.post(
        Urls.CREATE_ORDER,
        json=payload
    )


@allure.step("Получение списка заказов")
def get_orders_list():
    return requests.get(Urls.ORDERS_LIST)