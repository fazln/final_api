import pytest
import allure
from tests.test_data.delete_meme_data import DeleteMemeTestData


@allure.feature('Meme')
@allure.story('Delete one meme')
@allure.title('Удаление мема')
@pytest.mark.regress
@pytest.mark.parametrize('method', DeleteMemeTestData.delete_meme_positive_data)
def test_delete_meme(delete_meme, method, token, meme_id):
    delete_meme.delete_meme(method, token, meme_id)
    delete_meme.check_status_is_200()
    delete_meme.delete_meme_is_correct(meme_id)


@allure.feature('Meme')
@allure.story('Delete one meme')
@allure.title('Удаление мема с невалидными данными')
@pytest.mark.regress
@pytest.mark.parametrize('method, expected_exception', DeleteMemeTestData.delete_meme_negative_data)
def test_delete_meme_negative(delete_meme, method, meme_id, expected_exception, token):
    with pytest.raises(expected_exception):
        delete_meme.delete_meme(method, token, meme_id)
        if delete_meme.response.status_code == 401:
            delete_meme.check_user_unathorized()
        elif delete_meme.response.status_code == 405:
            delete_meme.check_method_not_allowed()


@allure.feature('Meme')
@allure.story('Put meme')
@allure.title('Удаления мема без авторизации')
@pytest.mark.regress
@pytest.mark.parametrize('method, expected_exception', DeleteMemeTestData.delete_meme_negative_data_no_auth)
def test_delete_meme_negative_no_auth(delete_meme, method, meme_id, expected_exception, token_negative):
    with pytest.raises(expected_exception):
        delete_meme.delete_meme(method, token_negative, meme_id)
        if delete_meme.response.status_code == 401:
            delete_meme.check_user_unathorized()
        elif delete_meme.response.status_code == 405:
            delete_meme.check_method_not_allowed()
