from src.utils.http_methods import Http_methods

"""Методы для тестирования json_place_holder"""

base_url = "https://jsonplaceholder.typicode.com"


class Json_placeholder():

    """ Метод для получения страницы posts """
    @staticmethod
    def get_json_placeholder_posts():
        get_resource = "/posts"
        get_url = base_url + get_resource
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """ Метод для создания нового пользователя """
    @staticmethod
    def create_new_user():
        json_for_create_new_user = {
            "userId": 10,
            "id": 101,
            "title": "STRING",
            "body": "Yes. This is a string"
        }

        post_resource = "/posts"  # ресурс для метода Post
        post_url = base_url + post_resource
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_user)
        print(result_post.text)
        return result_post

    """ Метод для удаления пользователя """
    @staticmethod
    def delete_user():
        delete_resource = "/posts/1"  # ресурс для метода Delete
        delete_url = base_url + delete_resource
        print(delete_url)
        result_delete = Http_methods.delete(delete_url)
        print(result_delete.text)
        return result_delete
