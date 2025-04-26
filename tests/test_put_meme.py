import pytest
import allure
from tests.test_data.put_meme_data import PutMemeTestData


@allure.feature('Meme')
@allure.story('Put meme')
@allure.title('Обновление мема')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PutMemeTestData.put_meme_positive_data)
def test_put_meme(put_meme, method, body, meme_id, token):
    body['id'] = meme_id
    put_meme.put_meme(method, body, meme_id, token)
    put_meme.check_status_is_200()
    put_meme.check_meme_is_correct(body['text'], body['url'], body['tags'], body['info'])


@allure.feature('Meme')
@allure.story('Put meme')
@allure.title('Обновление мема с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, body, expected_exception', PutMemeTestData.put_meme_negative_data)
def test_put_meme_negative(put_meme, method, body, meme_id, expected_exception, token):
    with pytest.raises(expected_exception):
        if 'id' in body:
            body['id'] = meme_id
        put_meme.put_meme(method, body, meme_id, token)
        if put_meme.response.status_code == 400:
            put_meme.check_bad_request()
        elif put_meme.response.status_code == 405:
            put_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Put meme')
@allure.title('Обновление мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method, body, expected_exception', PutMemeTestData.put_meme_negative_data_no_auth)
def test_put_meme_negative_no_auth(put_meme, method, body, meme_id, expected_exception, token_negative):
    with pytest.raises(expected_exception):
        if 'id' in body:
            body['id'] = meme_id
        put_meme.put_meme(method, body, meme_id, token_negative)
        if put_meme.response.status_code == 401:
            put_meme.check_user_unathorized()
        elif put_meme.response.status_code == 405:
            put_meme.check_method_not_allowed()
