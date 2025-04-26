import pytest
import allure
from tests.test_data.get_meme_data import GetMemeTestData


@allure.feature('Meme')
@allure.story('Get meme')
@allure.title('Получение всех мемов')
@pytest.mark.smoke
@pytest.mark.parametrize('method', GetMemeTestData.get_meme_positive_data)
def test_get_all_meme(get_meme, method, token):
    get_meme.get_all_meme(method, token)
    get_meme.check_status_is_200()


@allure.feature('Meme')
@allure.story('Get meme')
@allure.title('Получение всех мемов с невалидными данными')
@pytest.mark.smoke
@pytest.mark.parametrize('method, expected_exception', GetMemeTestData.get_meme_negative_data)
def test_get_all_meme_negative(get_meme, method, expected_exception, token_negative):
    with pytest.raises(expected_exception):
        get_meme.get_all_meme(method, token_negative)
        if get_meme.response.status_code == 401:
            get_meme.check_user_unathorized()
        elif get_meme.response.status_code == 405:
            get_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Get one meme')
@allure.title('Получение одного мема')
@pytest.mark.regress
@pytest.mark.parametrize('method', GetMemeTestData.get_meme_positive_data)
def test_get_one_meme(get_meme, method, token, meme_id):
    get_meme.get_one_meme(method, token, meme_id)
    get_meme.check_status_is_200()


@allure.feature('Meme')
@allure.story('Get one meme')
@allure.title('Получение одного мема с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, expected_exception', GetMemeTestData.get_one_meme_negative_data)
def test_get_one_meme_negative(get_meme, method, meme_id, expected_exception, token_negative):
    with pytest.raises(expected_exception):
        get_meme.get_one_meme(method, token_negative, meme_id)
        if get_meme.response.status_code == 401:
            get_meme.check_user_unathorized()
        elif get_meme.response.status_code == 405:
            get_meme.check_method_not_allowed()
