import pytest
from tests import test_create_user
from http import HTTPStatus

@pytest.mark.run(order=5)
def test_get_users_200(apis):
    response = apis.get("/public/v2/users")
    # print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert len(response.json())>0


@pytest.mark.run(order=6)
def test_get_single_user_200(apis):
    user_id = test_create_user.test_createuser(apis)
    response = apis.get(f"/public/v2/users/{user_id}")
    print(response.json())
    assert response.status_code == HTTPStatus.OK
    assert response.json()['name'] == "Anita Adibatti"

@pytest.mark.run(order=7)
def test_get_invalid_user_404(apis):
    user_id = str(test_create_user.test_createuser(apis))+"123"
    response = apis.get(f"/public/v2/users/{user_id}")
    print(response.json())
    assert response.status_code == HTTPStatus.NOT_FOUND

@pytest.mark.run(order=8)
def test_get_user_with_invalid_endpoints_404(apis):
    user_id = test_create_user.test_createuser(apis)
    response = apis.get(f"/public/v2/user/{user_id}")
    print(response.json())
    assert response.status_code == HTTPStatus.NOT_FOUND