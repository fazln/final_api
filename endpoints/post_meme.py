import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, UserUnathorized, InvalidDataError, MemeNotFound


class PostMeme(BaseEndpoint):
    meme_id = None

    @allure.step('Create new meme')
    def post_meme(self, method, payload, token):
        self.response = requests.request(
            method,
            f'{self.url}/meme',
            json=payload,
            headers={'Authorization': f'{token}'}
        )
        try:
            if self.response.status_code == 400:
                raise InvalidDataError('Invalid data format')
            elif self.response.status_code == 401:
                raise UserUnathorized('User unathorize')
            elif self.response.status_code == 404:
                raise MemeNotFound('Meme not found')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response

    @allure.step('Check meme is not created')
    def check_meme_not_create(self):
        assert 'text' not in self.json, 'Meme text is created'
        assert 'url' not in self.json, 'Meme url is created'
        assert 'tags' not in self.json, 'Meme tags are created'
        assert 'info' not in self.json, 'Meme info is created'