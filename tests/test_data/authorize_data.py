import random
import string


class AuthorizeTestData:
    positive_data = [
        ({'name': 'Jack'}, 'Post'),
        ({'name': 'R2 d2'}, 'Post'),
        ({'name': 'string'}, 'Post'),
    ]

    negative_data = [
        ({'name': 1}, 'Post'),
        ({'name': None}, 'Post'),
        ({'name': {1: 'name'}}, 'Post'),
        ({'name': ['test']}, 'Post'),
        ({'name': True}, 'Post'),
        ({'name': 2.3}, 'Post'),
    ]

    negative_method = [
        ({'name': '1'}, 'Get'),
        ({'name': {}}, 'Patch'),
        ({'name': []}, 'Put'),
        ({'name': 2.3}, 'Delete'),
    ]


class TokenAliveTestData:
    positive = [
        'Get'
    ]

    negative_method = [
        ('Put'),
        ('Post'),
        ('Patch'),
        ('Delete')
    ]

    token_negative = ''.join(random.choices(string.ascii_letters + string.digits, k=15))
    negative_token = [
        ('Get', token_negative)
    ]
