import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidDataError, InvalidMethodError, UserUnathorized


class PutMeme(BaseEndpoint):
    meme_id = None

    @allure.step('Update a meme')
    def put_meme(self, method, payload, meme_id, token):
        self.response = requests.request(
            method,
            f'{self.url}/meme/{meme_id}',
            json=payload,
            headers={'Authorization': f'{token}'}
        )
        if self.response.status_code == 400:
            raise InvalidDataError('Invalid data format')
        elif self.response.status_code == 401:
            raise UserUnathorized('User unathorize')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        else:
            self.json = self.response.json()
            return self.response
