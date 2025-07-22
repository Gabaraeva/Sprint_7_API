import pytest
import allure
from helpers import create_order, get_orders_list
from data import TestData

@allure.feature('Order Management')
class TestOrder:
    @pytest.mark.parametrize('color', [
        TestData.COLOR_BLACK,
        TestData.COLOR_GREY,
        TestData.BOTH_COLORS,
        TestData.NO_COLOR
    ])
    @allure.title('Create order with colors: {color}')
    def test_create_order_with_colors(self, color):
        response = create_order(color)
        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title('Get orders list')
    def test_get_orders_list(self):
        response = get_orders_list()
        assert response.status_code == 200
        assert isinstance(response.json()['orders'], list)
        assert len(response.json()['orders']) > 0