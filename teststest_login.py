import pytest
import allure
import requests
from helpers import register_new_courier, login_courier, delete_courier


@allure.feature('Courier Login')
class TestCourierLogin:
    @allure.title('Successful login')
    def test_login_success(self):
        courier = register_new_courier()
        response = login_courier(courier['login'], courier['password'])
        assert response.status_code == 200
        assert "id" in response.json()

        delete_courier(response.json()['id'])

    @allure.title('Login without required fields')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_missing_field(self, field):
        payload = {"login": "valid_login", "password": "valid_pass"}
        del payload[field]

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data=payload
        )
        assert response.status_code == 400
        assert "недостаточно данных" in response.json()["message"]

    @allure.title('Login with invalid credentials')
    @pytest.mark.parametrize('login,password,expected', [
        ('invalid', 'valid_pass', 404),
        ('valid_login', 'invalid', 404),
        ('nonexistent', 'user', 404)
    ])
    def test_login_invalid_credentials(self, login, password, expected):
        courier = register_new_courier()
        response = login_courier(login, password)
        assert response.status_code == expected
        assert "Учетная запись не найдена" in response.json()["message"]

        login_resp = login_courier(courier['login'], courier['password'])
        if login_resp.status_code == 200:
            delete_courier(login_resp.json()['id'])
