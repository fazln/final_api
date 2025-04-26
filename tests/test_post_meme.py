import pytest
import allure
from tests.test_data.post_meme_data import PostMemeTestData


@allure.feature('Meme')
@allure.story('Post meme')
@allure.title('Добавление нового мема')
@pytest.mark.smoke
@pytest.mark.parametrize('method, body', PostMemeTestData.post_meme_positive_data)
def test_post_meme(post_meme, method, body, token):
    post_meme.post_meme(method, body, token)
    post_meme.check_status_is_200()
    post_meme.check_meme_is_correct(body['text'], body['url'], body['tags'], body['info'])


@allure.feature('Meme')
@allure.story('Post meme')
@allure.title('Добавление нового мема c негативными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, body, expected_exception', PostMemeTestData.post_meme_negative_data)
def test_post_meme_negative(post_meme, method, body, expected_exception, token):
    with pytest.raises(expected_exception):
        post_meme.post_meme(method, body, token)
        if post_meme.response.status_code == 400:
            post_meme.check_bad_request()
        elif post_meme.response.status_code == 405:
            post_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Post meme')
@allure.title('Добавление нового мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method, body, expected_exception', PostMemeTestData.post_meme_negative_data_no_auth)
def test_post_meme_negative_no_auth(post_meme, method, body, expected_exception, token_negative):
    with pytest.raises(expected_exception):
        post_meme.post_meme(method, body, token_negative)
        if post_meme.response.status_code == 401:
            post_meme.check_user_unathorized()
        elif post_meme.response.status_code == 405:
            post_meme.check_method_not_allowed()
