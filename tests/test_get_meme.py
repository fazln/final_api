import pytest
import allure
from tests.test_data.get_meme_data import GetMemeTestData, GetOneMemeTestData
from endpoints.base_endpoint import UserUnathorized, InvalidMethodError


@allure.feature('Meme')
@allure.story('Get memes')
@allure.title('Получение всех мемов')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetMemeTestData.positive_data)
def test_get_all_meme(get_meme, method, token):
    get_meme.get_all_meme(method, token)
    get_meme.check_status_is_200()
    get_meme.check_get_memes()


@allure.feature('Meme')
@allure.story('Get memes negative')
@allure.title('Получение всех мемов с невалидным методом')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetMemeTestData.negative_method)
def test_get_all_meme_negative_method(get_meme, method, token):
    try:
        get_meme.get_all_meme(method, token)
    except InvalidMethodError:
        get_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Get memes negative')
@allure.title('Получение всех мемов без авторизации')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetMemeTestData.positive_data)
def test_get_all_meme_negative_token(get_meme, method, token_negative):
    try:
        get_meme.get_all_meme(method, token_negative)
    except UserUnathorized:
        get_meme.check_user_unathorized()


@allure.feature('Meme')
@allure.story('Get one meme')
@allure.title('Получение одного мема')
@pytest.mark.regress
@pytest.mark.parametrize('method', GetOneMemeTestData.positive_data)
def test_get_one_meme(get_meme, method, token, meme_id):
    get_meme.get_one_meme(method, token, meme_id)
    get_meme.check_get_one_meme(meme_id)
    get_meme.check_status_is_200()


@allure.feature('Meme')
@allure.story('Get one meme negative')
@allure.title('Получение одного мема с невалидным методом')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetOneMemeTestData.negative_method)
def test_get_one_meme_negative_method(get_meme, method, token, meme_id):
    try:
        get_meme.get_one_meme(method, token, meme_id)
    except InvalidMethodError:
        get_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Get one meme negative')
@allure.title('Получение одного мема без авторизации')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetOneMemeTestData.positive_data)
def test_get_one_meme_negative_token(get_meme, method, token_negative, meme_id):
    try:
        get_meme.get_one_meme(method, token_negative, meme_id)
    except UserUnathorized:
        get_meme.check_user_unathorized()
