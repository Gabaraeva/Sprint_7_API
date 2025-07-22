import pytest
import allure
from helpers import register_new_courier, login_courier, delete_courier

@pytest.fixture
def create_courier():
    """Фикстура для создания курьера (предусловие)"""
    with allure.step("Создание тестового курьера"):
        courier = register_new_courier()
        yield courier

@pytest.fixture
def delete_courier_after_test():
    """Фикстура для удаления курьера (постусловие)"""
    courier_ids = []
    yield
    with allure.step("Удаление тестовых курьеров"):
        for courier_id in courier_ids:
            delete_courier(courier_id)

@pytest.fixture
def authenticated_courier(create_courier, delete_courier_after_test):
    """Фикстура для авторизованного курьера"""
    courier = create_courier
    response = login_courier(courier['login'], courier['password'])
    courier_id = response.json()['id']
    delete_courier_after_test.courier_ids.append(courier_id)
    return {
        "login": courier['login'],
        "password": courier['password'],
        "id": courier_id
    }