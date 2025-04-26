from endpoints.authorize import InvalidMethodError, InvalidDataError, UserUnathorized


class PostMemeTestData:

    post_meme_positive_data = [
        ('Post',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}),
        ('Post',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {},
          "new_attr": 'test'}),
    ]

    post_meme_negative_data = [
        ('Post',
         {"url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         InvalidDataError),
        ('Post',
         {"text": 'test',
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         InvalidDataError),
        ('Post',
         {"url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "info": {"info": 1}},
         InvalidDataError),
         ('Post',
          {"text": 'test',
            "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                  "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                  "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                  "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
           "tags": ["univer", "study"]},
          InvalidDataError),
        ('Patch',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Delete',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Put',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
    ]

    post_meme_negative_data_no_auth = [
        ('Post',
         {"url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         UserUnathorized),
        ('Post',
         {"text": 'test',
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         UserUnathorized),
        ('Post',
         {"url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "info": {"info": 1}},
         UserUnathorized),
         ('Post',
          {"text": 'test',
            "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                  "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                  "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                  "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
           "tags": ["univer", "study"]},
          UserUnathorized),
        ('Patch',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Delete',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Put',
         {"text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
    ]