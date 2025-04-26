from endpoints.authorize import InvalidMethodError, InvalidDataError, UserUnathorized
from endpoints.post_meme import PostMeme


class PutMemeTestData(PostMeme):

    put_meme_positive_data = [
        ('Put',
         {"id": "",
          "text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}),
        ('Put',
         {"id": "",
          "text": "",
          "url": "",
          "tags": [],
          "info": {},
          "new_attr": 'test'}),
    ]

    put_meme_negative_data = [
        ('Put',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         InvalidDataError),
        ('Put',
         {"id": "",
          "text": 'test',
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         InvalidDataError),
        ('Put',
         {"id": "",
          "text": 'test',
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "info": {"info": 1}},
         InvalidDataError),
         ('Post',
          {"id": "",
           "text": 'test',
           "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                  "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                  "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                  "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
           "tags": ["univer", "study"]},
          InvalidMethodError),
        ('Patch',
         {"id": "",
          "text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Put',
         {"text": 2,
          "url": "",
          "tags": [],
          "info": {}},
         InvalidDataError),
    ]

    put_meme_negative_data_no_auth = [
        ('Put',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         UserUnathorized),
        ('Put',
         {"id": "",
          "text": 'test',
          "tags": ["univer", "study"],
          "info": {"info": 1}},
         UserUnathorized),
        ('Put',
         {"id": "",
          "text": 'test',
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "info": {"info": 1}},
         UserUnathorized),
        ('Post',
         {"id": "",
          "text": 'test',
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"]},
         InvalidMethodError),
        ('Patch',
         {"id": "",
          "text": "",
          "url": "",
          "tags": [],
          "info": {}},
         InvalidMethodError),
        ('Put',
         {"text": 2,
          "url": "",
          "tags": [],
          "info": {}},
         UserUnathorized),
    ]