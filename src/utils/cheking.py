import json

from requests import Response
"""Методы для проверки ответов наших запросов"""


class Cheking():

    """Метод для проверки статуса кодов"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code

    """Метод для проверки наличия полей в ответе запроса"""
    @staticmethod
    def check_json_token(result, expected_result):
        token = json.loads(result.text)
        assert list(token) == expected_result
        print('Все поля присутствуют')

    """Метод для подсчета количества записей"""
    @staticmethod
    def check_quantity(result, expected_result):
        token = json.loads(result.text)
        assert len(token) == expected_result
