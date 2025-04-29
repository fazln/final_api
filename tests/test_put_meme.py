import pytest
import allure
from tests.test_data.put_meme_data import PutMemeTestData
from endpoints.base_endpoint import InvalidDataError, InvalidMethodError, UserUnathorized, AccessForbidden


@allure.feature('Meme')
@allure.story('Update meme')
@allure.title('Обновление мема')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PutMemeTestData.positive_data)
def test_put_meme(put_meme, method, body, meme_id, token):
    body['id'] = meme_id
    put_meme.put_meme(method, body, meme_id, token)
    put_meme.check_status_is_200()
    put_meme.check_meme_is_correct(body['text'], body['url'], body['tags'], body['info'])


@allure.feature('Meme')
@allure.story('Update meme negative')
@allure.title('Обновление мема с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PutMemeTestData.negative_data)
def test_put_meme_negative_data(put_meme, method, body, meme_id, token):
    try:
        put_meme.put_meme(method, body, meme_id, token)
    except InvalidDataError:
        put_meme.check_bad_request()


@allure.feature('Meme')
@allure.story('Update meme negative')
@allure.title('Обновление мема с некорректным методом')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PutMemeTestData.negative_method)
def test_put_meme_negative_method(put_meme, method, body, meme_id, token):
    try:
        put_meme.put_meme(method, body, meme_id, token)
    except InvalidMethodError:
        put_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Update meme negative')
@allure.title('Обновление мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PutMemeTestData.negative_no_auth)
def test_put_meme_negative_token(put_meme, method, body, meme_id, token_negative):
    try:
        put_meme.put_meme(method, body, meme_id, token_negative)
    except UserUnathorized:
        put_meme.check_user_unathorized()


@allure.feature('Meme')
@allure.story('Update meme negative')
@allure.title('Обновление мема без прав')
@pytest.mark.regress
@pytest.mark.parametrize('method, body, data_auth, method_auth', PutMemeTestData.user_forbidden)
def test_put_meme_negative_forbidden(authorize, put_meme, method, body, data_auth, method_auth, meme_id):
    try:
        token_old = authorize.get_token(data_auth, method_auth).json()['token']
        body['id'] = meme_id
        put_meme.put_meme('Put', body, meme_id, token_old)
    except AccessForbidden:
        put_meme.check_access_forbidden()
