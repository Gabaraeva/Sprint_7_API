class TestData:
    # Сообщения об ошибках
    ALREADY_EXISTS_ERROR = "Этот логин уже используется. Попробуйте другой."
    MISSING_DATA_ERROR = "Недостаточно данных для создания учетной записи"
    LOGIN_MISSING_DATA = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"

    # Тестовые данные
    ORDER_DATA = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "Москва, Кремль, 1",
        "metroStation": 4,
        "phone": "+79999999999",
        "rentTime": 5,
        "deliveryDate": "2025-07-20",
        "comment": "Комментарий",
    }

    # Цвета для заказов
    COLOR_BLACK = ["BLACK"]
    COLOR_GREY = ["GREY"]
    BOTH_COLORS = ["BLACK", "GREY"]
    NO_COLOR = None