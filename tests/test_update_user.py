from http import HTTPStatus

import pytest
from tests import test_create_user


@pytest.mark.run(order=9)
def test_updateuser_200(apis):
    data = {
            'name':"Anita Nandeesh Adibatti",
            'email':apis.generate_email(),
            'gender':"female",
            'status':"active"
            }
    user_id = test_create_user.test_createuser(apis)
    response = apis.put(f"/public/v2/users/{user_id}",body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.OK
    updated_data = apis.get(f"/public/v2/users/{user_id}").json()
    assert updated_data['name'] == "Anita Nandeesh Adibatti"


@pytest.mark.run(order=10)
def test_update_invalid_user_404(apis):
    data = {
        'name': "Anita Nandeesh Adibatti",
        'email': apis.generate_email(),
        'gender': "female",
        'status': "active"
    }
    # user_id = test_create_user.test_createuser(apis)
    response = apis.put(f"/public/v2/users/123", body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.NOT_FOUND


@pytest.mark.run(order=11)
def test_updateuser_with_invalid_data_422(apis):
    data = {
            'name':"Anita Nandeesh Adibatti",
            'email':apis.generate_email(),
            'gender':123,
            'status':"active"
            }
    user_id = test_create_user.test_createuser(apis)
    response = apis.put(f"/public/v2/users/{user_id}",body=data)
    # json_data = response.json()
    assert response.status_code == HTTPStatus.UNPROCESSABLE_CONTENT
