import pytest
import allure
import requests
from helpers import generate_random_string
from urls import Urls
from data import TestData


@allure.feature('Courier Creation')
class TestCourierCreation:
    @allure.title('Successful courier creation')
    def test_create_courier_success(self, authenticated_courier, delete_courier_after_test):
        # Фикстура создает курьера и автоматически удалит его после теста
        assert authenticated_courier["id"] > 0

    @allure.title('Duplicate courier creation')
    def test_create_duplicate_courier(self, authenticated_courier, delete_courier_after_test):
        # Пытаемся создать дубликат курьера
        payload = {
            "login": authenticated_courier["login"],
            "password": "any_password",
            "firstName": "any_name"
        }

        response = requests.post(
            Urls.CREATE_COURIER,
            data=payload
        )
        assert response.status_code == 409
        assert TestData.ALREADY_EXISTS_ERROR in response.json()["message"]

    @pytest.mark.parametrize('field', ['login', 'password', 'firstName'])
    @allure.title('Missing required field: {field}')
    def test_create_courier_missing_field(self, field):
        data = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }
        del data[field]

        response = requests.post(
            Urls.CREATE_COURIER,
            data=data
        )
        assert response.status_code == 400
        assert TestData.MISSING_DATA_ERROR in response.json()["message"]