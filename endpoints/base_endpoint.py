import allure


class InvalidDataError(Exception):
    pass


class InvalidMethodError(Exception):
    pass


class InternalServerError(Exception):
    pass


class UserUnathorized(Exception):
    pass


class BaseEndpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None

    @allure.step('Check that response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Check that 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Status code is incorrect'

    @allure.step('Check that 401 error received')
    def check_user_unathorized(self):
        assert self.response.status_code == 401, 'Status code is incorrect'

    @allure.step('Check that 404 error received')
    def check_token_not_found(self):
        assert self.response.status_code == 404, 'Status code is incorrect'

    @allure.step('Check that 405 error received')
    def check_method_not_allowed(self):
        assert self.response.status_code == 405, 'Status code is incorrect'

    @allure.step('Check that 500 error received')
    def check_internal_server_error(self):
        assert self.response.status_code == 500, 'Status code is incorrect'

    @allure.step('Check user is correct')
    def check_user_is_correct(self, user):
        assert self.json['user'] == user, 'User is incorrect'

    @allure.step('Delete meme is correct')
    def delete_meme_is_correct(self, meme_id):
        assert self.response.text == f'Meme with id {meme_id} successfully deleted', 'Meme is not deleted'

    @allure.step('Check meme is correct')
    def check_meme_is_correct(self, text, url, tags, info):
        assert self.json['text'] == text, 'Meme text is incorrect'
        assert self.json['url'] == url, 'Meme url is incorrect'
        assert self.json['tags'] == tags, 'Meme tags are incorrect'
        assert self.json['info'] == info, 'Meme info is incorrect'
