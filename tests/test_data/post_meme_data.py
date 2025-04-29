class PostMemeTestData:

    positive_data = [
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

    negative_data = [
        ('Post',
         {"url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}),
        ('Post',
         {"text": 'test',
          "tags": ["univer", "study"],
          "info": {"info": 1}}),
        ('Post',
         {"text": 'test',
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "info": {"info": 1}}),
         ('Post',
          {"text": 'test',
            "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                  "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                  "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                  "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
           "tags": ["univer", "study"]}),
        ('Post',
         {}),
        ('Post',
         {"text": 1,
          "url": 2,
          "tags": '[]',
          "info": True})
    ]

    negative_method = [
        ('Patch',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}
         ),
        ('Put',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}
         ),
        ('Delete',
         {"text": "John",
          "url": "https://sun9-10.userapi.com/s/v1/if1/6C2luVD7eqbwelkPgv6HlHkGsIHSmucX_l"
                 "eK4ybQp9tgMuHKaHHw5k1n7p1-E_FcjHaP7fUW.jpg?quality=96&as=32x32,48x47,72"
                 "x71,108x107,160x158,240x237,360x355,480x474,540x533,640x632,720x711,108"
                 "0x1066&from=bu&u=5b_1en06950-867pW_jFQmSKUfNsza8kNQIpJ2DnLqQ&cs=807x797",
          "tags": ["univer", "study"],
          "info": {"info": 1}}
         )
    ]

    negative_no_auth = [
        ('Post',
         {"text": "text_1",
          "url": "url_1",
          "tags": ['tags'],
          "info": {}}
         )
    ]