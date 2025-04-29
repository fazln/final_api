class GetMemeTestData:

    positive_data = [
        ('Get')
    ]

    negative_method = [
        ('Put'),
        ('Patch'),
        ('Delete')
    ]


class GetOneMemeTestData:

    positive_data = [
        ('Get')
    ]

    negative_method = [
        ('POST'),
        ('Patch'),
    ]