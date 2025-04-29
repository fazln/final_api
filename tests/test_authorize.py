import pytest
import allure
from tests.test_data.authorize_data import AuthorizeTestData, TokenAliveTestData
from endpoints.base_endpoint import InvalidMethodError, UserUnathorized, InvalidDataError


@allure.feature('Authorize')
@allure.story('Get token')
@allure.title('Получение токена для пользователя')
@pytest.mark.smoke
@pytest.mark.parametrize('data, method', AuthorizeTestData.positive_data)
def test_get_token(authorize, data, method):
    authorize.get_token(data, method)
    authorize.check_status_is_200()
    authorize.check_user_is_correct(data['name'])
    authorize.check_get_token()


@allure.feature('Authorize')
@allure.story('Get token negative method')
@allure.title('Получение токена с некорректным методом')
@pytest.mark.regress
@pytest.mark.parametrize('negative_method, method', AuthorizeTestData.negative_method)
def test_get_token_negative_method(authorize, negative_method, method):
    try:
        authorize.get_token(negative_method, method)
    except InvalidMethodError:
        authorize.check_method_not_allowed()


@allure.feature('Authorize')
@allure.story('Get token negative data')
@allure.title('Получение токена с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('negative_data, method', AuthorizeTestData.negative_data)
def test_get_token_negative_data(authorize, negative_data, method):
    try:
        authorize.get_token(negative_data, method)
    except InvalidDataError:
        authorize.check_bad_request()


@allure.feature('Authorize')
@allure.story('Get token status')
@allure.title('Проверка жизни токена')
@pytest.mark.sanity
@pytest.mark.parametrize('method', TokenAliveTestData.positive)
def test_token_alive(get_token_status, method, token):
    get_token_status.token_status(method, token)
    get_token_status.check_status_is_200()


@allure.feature('Authorize')
@allure.story('Get token status negative data')
@allure.title('Проверка жизни токена с невалидным токеном')
@pytest.mark.regress
@pytest.mark.parametrize('method, negative_token', TokenAliveTestData.negative_token)
def test_token_alive_negative_token(get_token_status, method, negative_token):
    try:
        get_token_status.token_status(method, negative_token)
    except UserUnathorized:
        get_token_status.check_token_not_found()


@allure.feature('Authorize')
@allure.story('Get token status negative method')
@allure.title('Проверка жизни токена с некорректным методом')
@pytest.mark.sanity
@pytest.mark.parametrize('method', TokenAliveTestData.negative_method)
def test_token_alive_negative_method(get_token_status, method, token):
    try:
        get_token_status.token_status(method, token)
    except InvalidMethodError:
        get_token_status.check_method_not_allowed()
