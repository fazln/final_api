import pytest
import allure
from tests.test_data.authorize_data import AuthorizeTestData


@allure.feature('Authorize')
@allure.story('Get token')
@allure.title('Получение токена для пользователя')
@pytest.mark.smoke
@pytest.mark.parametrize('data, method', AuthorizeTestData.get_token_positive_data)
def test_get_token(authorize, data, method):
    authorize.get_token(data, method)
    authorize.check_status_is_200()
    authorize.check_user_is_correct(data['name'])


@allure.feature('Authorize')
@allure.story('Get token')
@allure.title('Получение токена с негативными данными')
@pytest.mark.regress
@pytest.mark.parametrize('negative_data, method, expected_exception', AuthorizeTestData.get_token_negative_data)
def test_get_token_negative(authorize, expected_exception, negative_data, method):
    with pytest.raises(expected_exception):
        authorize.get_token(negative_data, method)
        if authorize.response.status_code == 400:
            authorize.check_bad_request()
        elif authorize.response.status_code == 405:
            authorize.check_method_not_allowed()


@allure.feature('Authorize')
@allure.story('Get token')
@allure.title('Проверка жизни токена')
@pytest.mark.sanity
@pytest.mark.parametrize('method', AuthorizeTestData.check_token_alive_positive)
def test_check_token_alive(get_token_status, token, method):
    get_token_status.token_status(method, token)
    get_token_status.check_status_is_200()


@allure.feature('Authorize')
@allure.story('Get token')
@allure.title('Проверка жизни токена с невалидными данными')
@pytest.mark.sanity
@pytest.mark.parametrize('method, expected_exception', AuthorizeTestData.check_token_alive_negative)
def test_check_token_alive_negative(get_token_status, token, method, expected_exception):
    with pytest.raises(expected_exception):
        get_token_status.token_status(method, token)
        if get_token_status.response.status_code == 405:
            get_token_status.check_method_not_allowed()
        elif get_token_status.response.status_code == 404:
            get_token_status.check_token_not_found()
