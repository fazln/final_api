import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, UserUnathorized, InvalidDataError


class Authorize(BaseEndpoint):
    token = None
    method = None

    @allure.step('Authorize user')
    def get_token(self, payload, method):
        self.response = requests.request(
            method,
            f'{self.url}/authorize',
            json=payload,
        )
        try:
            if self.response.status_code == 400:
                raise InvalidDataError('Invalid data format')
            elif self.response.status_code == 401:
                raise UserUnathorized('User unathorized')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response

    @allure.step('Check get')
    def check_get_token(self):
        assert 'token' in self.json, 'Token is not in response'


class TokenLife(Authorize):
    @allure.step('Get token status')
    def token_status(self, method, token):
        self.response = requests.request(
            method,
            f'{self.url}/authorize/{token}'
        )
        try:
            if self.response.status_code == 400:
                raise InvalidDataError('Invalid data format')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response
