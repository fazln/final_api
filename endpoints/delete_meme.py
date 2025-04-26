import requests
import allure
from endpoints.base_endpoint import BaseEndpoint, InvalidMethodError, UserUnathorized


class DeleteMeme(BaseEndpoint):

    @allure.step('Delete meme')
    def delete_meme(self, method, token, meme_id):
        self.response = requests.request(
            method,
            f'{self.url}/meme/{meme_id}',
            headers={'Authorization': f'{token}'}
        )
        if self.response.status_code == 401:
            raise UserUnathorized('User unathorized')
        elif self.response.status_code == 405:
            raise InvalidMethodError('Method not allowed')
        else:
            return self.response
