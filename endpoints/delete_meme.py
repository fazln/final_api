import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, UserUnathorized, AccessForbidden, MemeNotFound


class DeleteMeme(BaseEndpoint):

    @allure.step('Delete meme')
    def delete_meme(self, method, token, meme_id):
        self.response = requests.request(
            method,
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{token}'}
        )
        try:
            if self.response.status_code == 401:
                raise UserUnathorized('User unathorized')
            elif self.response.status_code == 403:
                raise AccessForbidden('User not have access')
            elif self.response.status_code == 404:
                raise MemeNotFound('Meme not found')
            elif self.response.status_code == 405:
                raise InvalidMethodError('Method not allowed')
            else:
                self.json = self.response.json()
        except requests.exceptions.JSONDecodeError:
            self.json = {}
        return self.response

    @allure.step('Delete meme is correct')
    def delete_meme_is_correct(self, meme_id):
        assert self.response.text == f'Meme with id {meme_id} successfully deleted', 'Meme is not deleted'