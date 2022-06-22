import requests
import sys
import traceback
import urllib


def shorten():
    url_long = "https://docs.google.com/presentation/d/1Tlv2qfcXQba6IHakaD43qiDWFXaMRlAgmF95XYsZiGE/edit#slide=id.g122ee7e564b_0_5"
    URL = "http://tinyurl.com/api-create.php"
    try:
        url = URL + "?" \
            + urllib.parse.urlencode({"url": url_long})
        res = requests.get(url)
        print("STATUS CODE:", res.status_code)
        print("LONG URL:", url_long)
        print("SHORT URL:", res.text)
    except Exception as e:
        raise


print(shorten())


