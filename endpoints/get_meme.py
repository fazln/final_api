import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, InternalServerError, UserUnathorized


class GetMeme(BaseEndpoint):

    @allure.step('Get all meme')
    def get_all_meme(self, method, token):
        self.response = requests.request(
            method,
            f'{self.url}/meme',
            headers={'Authorization': f'{token}'}
        )
        if self.response.status_code == 401:
            raise UserUnathorized('User unathorized')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        elif self.response.status_code == 500:
            raise InternalServerError('The server was unable to complete your request')
        else:
            self.json = self.response.json()
            return self.response

    @allure.step('Get one meme')
    def get_one_meme(self, method, token, meme_id):
        self.response = requests.request(
            method,
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{token}'}
        )
        if self.response.status_code == 401:
            raise UserUnathorized('User unathorized')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        elif self.response.status_code == 500:
            raise InternalServerError('The server was unable to complete your request')
        else:
            self.json = self.response.json()
            return self.response
