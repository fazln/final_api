from endpoints.authorize import InvalidMethodError, UserUnathorized


class GetMemeTestData:

    get_meme_positive_data = [
        ('Get')
    ]

    get_meme_negative_data = [
        ('Put', InvalidMethodError),
        ('POST', UserUnathorized),
        ('Patch', InvalidMethodError),
        ('Delete', InvalidMethodError)
    ]

    get_one_meme_negative_data = [
        ('Put', UserUnathorized),
        ('POST', InvalidMethodError),
        ('Patch', InvalidMethodError),
        ('Delete', UserUnathorized)
    ]