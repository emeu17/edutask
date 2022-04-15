import pytest
import unittest.mock as mock

from src.controllers.usercontroller import UserController

# # tests for the get_user_by_email method
# @pytest.mark.demo
# @pytest.mark.parametrize('str, expected', [('jane.doe@gmail.com', 'jane.doe@gmail.com'), ('test@inget.se', None)])
# def test_get_user_by_email_true(obj, expected):
#     assert UserController.get_user_by_email(str, 'jane@doe.se') == expected

# tests for the get_user_by_email method
# adding as many user objects as passed in under amount,
# each object only contains email address
@pytest.fixture
def sut(email: str, amount: int):
    mockedusercontroller = mock.MagicMock()
    # create list of user-objects and add as many as amount sais
    users = []
    for x in range(amount):
        print(x)
        users.append({'email': email})
    # return the list of users from the doa object,
    # the length of the list will be checked
    mockedusercontroller.find.return_value = users
    mockedsut = UserController(dao=mockedusercontroller)
    return mockedsut

@pytest.mark.demo
# this creates an error because when no user is found then it would not be possible to return user[0]
# IndexError: list index out of range
@pytest.mark.parametrize('email, amount, expected', [('test@test.se', 1, {'email': 'test@test.se'}), ('test@test.se', 2, {'email': 'test@test.se'}), ('test@test.se', 0, None)])
def test_get_user_by_email(sut, expected):
    validationresult = sut.get_user_by_email(email="test@test.se")
    assert validationresult == expected
