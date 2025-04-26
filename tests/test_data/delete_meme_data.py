from endpoints.authorize import InvalidMethodError, UserUnathorized


class DeleteMemeTestData:

    delete_meme_positive_data = [
        ('Delete')
    ]
    delete_meme_negative_data = [
        ('Patch', InvalidMethodError),
    ]
    delete_meme_negative_data_no_auth = [
        ('Put', UserUnathorized),
        ('POST', InvalidMethodError),
        ('Patch', InvalidMethodError),
        ('Get', UserUnathorized)
    ]
