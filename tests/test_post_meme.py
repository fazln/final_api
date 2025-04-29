import pytest
import allure
from tests.test_data.post_meme_data import PostMemeTestData
from endpoints.base_endpoint import InvalidDataError, MemeNotFound, InvalidMethodError, UserUnathorized


@allure.feature('Meme')
@allure.story('Post meme')
@allure.title('Добавление нового мема')
@pytest.mark.smoke
@pytest.mark.parametrize('method, body', PostMemeTestData.positive_data)
def test_post_meme(post_meme, get_meme, method, body, token):
    meme_id = post_meme.post_meme(method, body, token).json()['id']
    post_meme.check_status_is_200()
    post_meme.check_meme_is_correct(body['text'], body['url'], body['tags'], body['info'])
    get_meme.get_one_meme('Get', token, meme_id)


@allure.feature('Meme')
@allure.story('Post meme negative')
@allure.title('Добавление нового мема c невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PostMemeTestData.negative_data)
def test_post_meme_negative_data(post_meme, method, body, token):
    try:
        post_meme.post_meme(method, body, token)
    except InvalidDataError:
        post_meme.check_bad_request()
    except MemeNotFound:
        post_meme.check_meme_not_create()


@allure.feature('Meme')
@allure.story('Post meme negative')
@allure.title('Добавление нового мема c некорректным методом')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PostMemeTestData.negative_method)
def test_post_meme_negative_method(post_meme, method, body, token):
    try:
        post_meme.post_meme(method, body, token)
    except InvalidMethodError:
        post_meme.check_method_not_allowed()
    except MemeNotFound:
        post_meme.check_meme_not_create()


@allure.feature('Meme')
@allure.story('Post meme')
@allure.title('Добавление нового мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method, body', PostMemeTestData.negative_no_auth)
def test_post_meme_negative_token(post_meme, method, body, token_negative):
    try:
        post_meme.post_meme(method, body, token_negative)
    except UserUnathorized:
        post_meme.check_user_unathorized()
    except MemeNotFound:
        post_meme.check_meme_not_create()
