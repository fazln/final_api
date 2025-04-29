import pytest
import allure
from tests.test_data.delete_meme_data import DeleteMemeTestData
from tests.test_data.authorize_data import AuthorizeTestData
from endpoints.base_endpoint import UserUnathorized, InvalidMethodError, MemeNotFound, AccessForbidden


@allure.feature('Meme')
@allure.story('Delete meme')
@allure.title('Удаление мема')
@pytest.mark.regress
@pytest.mark.parametrize('method', DeleteMemeTestData.positive_data)
def test_delete_meme(delete_meme, get_meme, method, token, meme_id):
    try:
        delete_meme.delete_meme(method, token, meme_id)
        delete_meme.check_status_is_200()
        delete_meme.delete_meme_is_correct(meme_id)
    except MemeNotFound:
        get_meme.check_get_one_meme(meme_id)


@allure.feature('Meme')
@allure.story('Delete meme negative')
@allure.title('Удаление мема с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('negative_method', DeleteMemeTestData.negative_method)
def test_delete_meme_negative_method(delete_meme, negative_method, meme_id, token):
    try:
        delete_meme.delete_meme(negative_method, token, meme_id)
    except InvalidMethodError:
        delete_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Delete meme negative')
@allure.title('Удаления мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method', DeleteMemeTestData.negative_data_no_auth)
def test_delete_meme_negative_token(delete_meme, method, meme_id, token_negative):
    try:
        delete_meme.delete_meme(method, token_negative, meme_id)
    except UserUnathorized:
        delete_meme.check_user_unathorized()


@allure.feature('Meme')
@allure.story('Delete meme negative')
@allure.title('Удаления мема без прав')
@pytest.mark.regress
@pytest.mark.parametrize('data, method', AuthorizeTestData.positive_data)
def test_delete_meme_negative_forbidden(authorize, delete_meme, data, method, meme_id):
    try:
        token_old = authorize.get_token(data, method).json()['token']
        delete_meme.delete_meme('Delete', token_old, meme_id)
    except AccessForbidden:
        delete_meme.check_access_forbidden()
