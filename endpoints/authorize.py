import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidDataError, InvalidMethodError, UserUnathorized


class Authorize(BaseEndpoint):
    token = None
    method = None

    @allure.step('Authorize')
    def get_token(self, payload, method):
        self.response = requests.request(
            method,
            f'{self.url}/authorize',
            json=payload,
        )
        if self.response.status_code == 400:
            raise InvalidDataError('Invalid data format')
        elif self.response.status_code == 401:
            raise UserUnathorized('User unathorized')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        else:
            self.json = self.response.json()
            self.token = self.json['token']
            return self.response


class TokenLife(Authorize):
    @allure.step('Get token status')
    def token_status(self, method, token):
        self.response = requests.request(
            method,
            f'{self.url}/authorize/{token}'
        )
        if self.response.status_code == 400:
            raise InvalidDataError('Invalid data format')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        else:
            return self.response
