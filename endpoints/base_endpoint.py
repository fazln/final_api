import allure


class InvalidDataError(Exception):
    pass


class InvalidMethodError(Exception):
    pass


class InternalServerError(Exception):
    pass


class UserUnathorized(Exception):
    pass


class MemeNotFound(Exception):
    pass


class AccessForbidden(Exception):
    pass


class BaseEndpoint:
    url = 'http://167.172.172.115:52355'
    response = None
    json = None

    @allure.step('Check response is 200')
    def check_status_is_200(self):
        assert self.response.status_code == 200, 'Status code is incorrect'

    @allure.step('Check 400 error received')
    def check_bad_request(self):
        assert self.response.status_code == 400, 'Status code is incorrect'

    @allure.step('Check 401 error received')
    def check_user_unathorized(self):
        assert self.response.status_code == 401, 'Status code is incorrect'

    @allure.step('Check 403 error received')
    def check_access_forbidden(self):
        assert self.response.status_code == 403, 'Status code is incorrect'

    @allure.step('Check 404 error received')
    def check_token_not_found(self):
        assert self.response.status_code == 404, 'Status code is incorrect'

    @allure.step('Check 405 error received')
    def check_method_not_allowed(self):
        assert self.response.status_code == 405, 'Status code is incorrect'

    @allure.step('Check user is correct')
    def check_user_is_correct(self, user):
        assert self.json['user'] == user, 'User is incorrect'

    @allure.step('Check meme is correct')
    def check_get_one_meme(self, meme_id):
        assert self.json['id'] == meme_id, 'Meme is not get'

    @allure.step('Check meme is correct')
    def check_meme_is_correct(self, text, url, tags, info):
        assert self.json['text'] == text, 'Meme text is incorrect'
        assert self.json['url'] == url, 'Meme url is incorrect'
        assert self.json['tags'] == tags, 'Meme tags are incorrect'
        assert self.json['info'] == info, 'Meme info is incorrect'
