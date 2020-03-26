import os as _os

ceefax_path = _os.path.dirname(_os.path.realpath(__file__))

pages_dir = _os.path.join(ceefax_path, "pages")
with open(_os.path.join(ceefax_path, "VERSION")) as f:
    VERSION = f.read()

NAME = "28JHFAX"

flight_api = "http://example.com/{}{}{}"

title =("-------yyyyyyyyyyyyyyyyy---------yyyyyyyyyy--------yyyyyyyyyy---------\n"
        "-------yyyyyyyyyyyyyyyyy---------yyyyyyyyyy--------yyyyyyyyyy---------\n"
        "-------yy......y......yy-----------y..yy.yy----------y.....yy---------\n"
        "-------yyyyyyy.y..yyy.yy-yyyyyyyyy-y..yy.yy-yyyyyyyy-y..yy.yy-yyyyyyyy\n"
        "-------yy......y......yy-yyyyyyyyy-y.....yy-yyyyyyyy-y.....yy-yyyyyyyy\n"
        "-------yy..yyyyy..yyy.yy-yyyyy..yy-y..yy.yy-y.....yy-y..yy.yy-y..y..yy\n"
        "-------yy......y......yy-yyyyy..yy-y..yy.yy-y..yyyyy-y..yy.yy-y..y..yy\n"
        "-------yyyyyyyyyyyyyyyyy-yyyyy..yy-yyyyyyyy-y....yyy-yyyyyyyy-yy...yyy\n"
        "-------yyyyyyyyyyyyyyyyy-y..yy..yy-yyyyyyyy-y..yyyyy-yyyyyyyy-y..y..yy\n"
        "-------------------------y......yy----------y..yyyyy----------y..y..yy\n"
        "-----------------------yyyyyyyyyyy--------yyyyyyyyyy--------yyyyyyyyyy\n"
        "-----------------------yyyyyyyyyyy--------yyyyyyyyyy--------yyyyyyyyyy").replace(".","b")


twitter_access_key = None
twitter_access_secret = None
twitter_consumer_key = None
twitter_consumer_secret = None

metoffer_api_key = None
open_weather_api_key = None

twitch_client_id = None

location = [51.5252257441084, -0.134831964969635]

try:
    from localconfig import *
except ImportError:
    pass
