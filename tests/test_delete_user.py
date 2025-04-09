import pytest
from tests import test_create_user

@pytest.mark.run(order=12)
def test_deleteuser(apis):
    user_id = test_create_user.test_createuser(apis)
    response = apis.delete(f"/public/v2/users/{user_id}")
    # print(response.json())
    assert response.status_code == 204
    status = apis.get(f"/public/v2/users/{user_id}").status_code
    assert status == 404