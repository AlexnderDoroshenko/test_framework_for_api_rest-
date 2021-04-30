import pytest
from src.helpers.api.users import Users


class TestPost:

    def test_user_create(self):
        body = {
            "name": "Gemini Varma",
            "email": "gemini_varma@johnston.net",
            "gender": "Female",
            "status": "Active",
        }
        response_obj = Users().post_user(body=body)
        assert response_obj.status_code == 200


class TestGet:
    def test_user_get(self):
        user = 15
        response_obj = Users().get_user(user)
        assert response_obj.status_code == 200


class TestPut:
    def test_user_update(self):
        user = 15
        response_obj = Users().put_user(user)
        assert response_obj.status_code == 200


class TestDelete:
    def test_user_delete(self):
        user = 15
        response_obj = Users().delete_user(user)
        assert response_obj.status_code == 200


