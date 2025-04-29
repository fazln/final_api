import pytest
from endpoints.authorize import Authorize
from endpoints.authorize import TokenLife
from endpoints.get_meme import GetMeme
from endpoints.post_meme import PostMeme
from endpoints.put_meme import PutMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.base_endpoint import MemeNotFound


@pytest.fixture(scope='session')
def authorize():
    return Authorize()


@pytest.fixture(scope='session')
def token(authorize):
    body = {
        "name": "John",
    }
    response = authorize.get_token(body, 'Post')
    token = response.json()['token']
    return token


@pytest.fixture()
def meme_id(token, get_meme):
    body = {
        "text": "John",
        "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_leK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,1080x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
        "tags": ["univer", "study"],
        "info": {}
    }
    response = PostMeme().post_meme('Post', body, token)
    meme_id = response.json()['id']
    yield meme_id

    try:
        DeleteMeme().delete_meme('Delete', token, meme_id)
    except MemeNotFound:
        print(f"\nMeme {meme_id} not found")


@pytest.fixture(scope='session')
def token_negative():
    return {}


@pytest.fixture()
def get_token_status():
    return TokenLife()


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
