from endpoints.authorize import InvalidDataError, InvalidMethodError


class AuthorizeTestData:
    get_token_positive_data = [
        ({'name': 'Jack'}, 'Post'),
        ({'name': 'R2 d2'}, 'Post'),
        ({'name': 'string'}, 'Post'),
    ]

    get_token_negative_data = [
        ({'name': 1}, 'Post', InvalidDataError),
        ({'name': '1'}, 'Get', InvalidMethodError),
        ({'name': {}}, 'Patch', InvalidMethodError),
        ({'name': []}, 'Get', InvalidMethodError),
        ({'name': True}, 'Post', InvalidDataError),
        ({'name': 2.3}, 'Delete', InvalidMethodError),
    ]

    check_token_alive_positive = [
        'Get'
    ]

    check_token_alive_negative = [
        ('Put', InvalidMethodError),
        ('Post', InvalidMethodError)
    ]
