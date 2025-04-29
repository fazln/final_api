import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, UserUnathorized, MemeNotFound


class GetMeme(BaseEndpoint):

    @allure.step('Get all meme')
    def get_all_meme(self, method, token):
        self.response = requests.request(
            method,
            f'{self.url}/meme',
            headers={'Authorization': f'{token}'}
        )
        try:
            if self.response.status_code == 401:
                raise UserUnathorized('User unathorized')
            elif self.response.status_code == 404:
                raise MemeNotFound('Meme not found')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response

    @allure.step('Check get memes')
    def check_get_memes(self):
        assert len(self.json['data']) != 0, 'Memes are not get'

    @allure.step('Get one meme')
    def get_one_meme(self, method, token, meme_id):
        self.response = requests.request(
            method,
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{token}'}
        )
        try:
            if self.response.status_code == 401:
                raise UserUnathorized('User unathorized')
            elif self.response.status_code == 404:
                raise MemeNotFound('Meme not found')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response
