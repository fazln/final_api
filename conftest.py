import pytest
import requests
from endpoints.authorize import Authorize
from endpoints.base_endpoint import InvalidDataError
from endpoints.base_endpoint import InvalidMethodError
from endpoints.authorize import TokenLife
from endpoints.get_meme import GetMeme
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope='session')
def authorize():
    return Authorize()


@pytest.fixture(scope='session')
def token():
    body = {
        "name": "John",
    }
    response = requests.post(
        'http://167.172.172.115:52355/authorize',
        json=body,
    )
    token = response.json()['token']
    yield token
    requests.delete(f'http://167.172.172.115:52355/meme/{token}')


@pytest.fixture()
def meme_id(token):
    body = {
        "text": "John",
        "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_leK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,1080x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
        "tags": ["univer", "study"],
        "info": {}
    }
    response = requests.post(
        'http://167.172.172.115:52355/meme',
        json=body,
        headers={'Authorization': f'{token}'}
    )
    meme_id = response.json()['id']
    yield meme_id
    requests.delete(f'http://167.172.172.115:52355/meme/{meme_id}')


@pytest.fixture(scope='session')
def token_negative():
    return {}


@pytest.fixture()
def get_token_status():
    return TokenLife()


@pytest.fixture()
def process_invalid_data():
    return InvalidDataError


@pytest.fixture()
def process_invalid_method():
    return InvalidMethodError


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def post_meme():
    return PostMeme()


@pytest.fixture()
def put_meme():
    return PutMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()
