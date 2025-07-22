import pytest
import allure
import requests
from urls import Urls
from data import TestData


@allure.feature('Courier Login')
class TestCourierLogin:
    @allure.title('Successful login')
    def test_login_success(self, authenticated_courier):
        # Фикстура уже выполнила вход, просто проверяем
        assert authenticated_courier["id"] > 0

    @allure.title('Login without required fields')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_login_missing_field(self, field):
        payload = {"login": "valid_login", "password": "valid_pass"}
        del payload[field]

        response = requests.post(
            Urls.LOGIN_COURIER,
            data=payload
        )
        assert response.status_code == 400
        assert TestData.LOGIN_MISSING_DATA in response.json()["message"]

    @allure.title('Login with invalid credentials')
    @pytest.mark.parametrize('login,password,expected', [
        ('invalid', 'valid_pass', 404),
        ('valid_login', 'invalid', 404),
        ('nonexistent', 'user', 404)
    ])
    def test_login_invalid_credentials(self, login, password, expected):
        response = requests.post(
            Urls.LOGIN_COURIER,
            data={"login": login, "password": password}
        )
        assert response.status_code == expected
        assert TestData.ACCOUNT_NOT_FOUND in response.json()["message"]