from src.utils.api import Json_placeholder
from src.utils.cheking import Cheking


def test_get_posts():

    print('Метод GET')
    result_get = Json_placeholder.get_json_placeholder_posts()
    Cheking.check_status_code(result_get, 200)
    Cheking.check_quantity(result_get, 100)


def test_create_new_user():

    print("Метод POST")
    result_post = Json_placeholder.create_new_user()
    Cheking.check_status_code(result_post, 201)
    Cheking.check_json_token(result_post, ['userId', 'id', 'title', 'body'])


def test_delete():

    print("Метод DELETE")
    result_delete = Json_placeholder.delete_user()
    Cheking.check_status_code(result_delete, 200)
    Cheking.check_json_token(result_delete, [])

