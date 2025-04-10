import pytest

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
    assert response.status_code == 201
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
    assert response.status_code == 404
#     404

@pytest.mark.run(order=3)
def test_create_user_with_invalid_data(apis):
    data = {
        # 'name': 123456,
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    response = apis.post("/public/v2/users", body=data)
    # json_data = response.json()
    assert response.status_code == 422
    # 422

@pytest.mark.run(order=4)
def test_create_user_with_invalid_method(apis): #need to try with put and delete
    data = {
        'name': "Anita Adibatti",
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    response = apis.get("/public/v2/users", body=data)
    # json_data = response.json()
    assert response.status_code == 201
