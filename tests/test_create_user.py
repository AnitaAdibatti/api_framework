import pytest
import requests
# requests.status_cod
from http import HTTPStatus

@pytest.mark.run(order=1)
def test_createuser(apis):
    data = {
            'name':"Anita Adibatti",
            'email':apis.generate_email(),
            'gender':"female",
            'status':"active"
            }
    response = apis.post("/public/v2/users",body=data)
    json_data = response.json()
    assert response.status_code == HTTPStatus.CREATED
    return json_data["id"]

@pytest.mark.run(order=2)
def test_create_user_with_invalid_endpoint(apis):
    data = {
        'name': "Anita Adibatti",
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    response = apis.post("/public/v2/user", body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.NOT_FOUND
#     404

@pytest.mark.run(order=3)
def test_create_user_with_invalid_data_422(apis):
    data = {
        # 'name': 123456,
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    response = apis.post("/public/v2/users", body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT
    # 422

@pytest.mark.run(order=4)
def test_create_user_with_invalid_method_405(apis): #need to try with put and delete
    data = {
        'name': "Anita Adibatti",
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    response = apis.get("/public/v2/users", body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED


def test_createuser_without_token_401(apis):
    data = {
            'name':"Anita Adibatti",
            'email':apis.generate_email(),
            'gender':"female",
            'status':"active"
            }
    url = "https://gorest.co.in/public/v2/users"
    response = requests.post(url,data=data)
    json_data = response.json()
    assert response.status_code == HTTPStatus.UNAUTHORIZED


