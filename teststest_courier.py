import pytest
import allure
import requests
from helpers import register_new_courier, login_courier, delete_courier, generate_random_string


@allure.feature('Courier Creation')
class TestCourierCreation:
    @allure.title('Successful courier creation')
    def test_create_courier_success(self):
        courier = register_new_courier()
        assert courier.get('login'), "Courier not created"
        response = courier['response']
        assert response.status_code == 201
        assert response.json() == {"ok": True}

        login_resp = login_courier(courier['login'], courier['password'])
        courier_id = login_resp.json()['id']
        delete_courier(courier_id)

    @allure.title('Duplicate courier creation')
    def test_create_duplicate_courier(self):
        courier = register_new_courier()
        assert courier.get('login'), "Initial courier not created"

        duplicate_response = register_new_courier()['response']
        assert duplicate_response.status_code == 409
        assert "уже существует" in duplicate_response.json()["message"]

        login_resp = login_courier(courier['login'], courier['password'])
        courier_id = login_resp.json()['id']
        delete_courier(courier_id)

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
            'https://qa-scooter.praktikum-services.ru/api/v1/courier',
            data=data
        )
        assert response.status_code == 400
        assert "недостаточно данных" in response.json()["message"]
