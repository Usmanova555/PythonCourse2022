import requests
import sys
import traceback
import urllib


class UrlShortenTinyurl:
    URL = "http://tinyurl.com/api-create.php"

    def shorten(self, url_long):

        try:
            url = self.URL + "?" \
                + urllib.parse.urlencode({"url": url_long})
            res = requests.get(url)
            print("STATUS CODE:", res.status_code)
            print("   LONG URL:", url_long)
            print("  SHORT URL:", res.text)
        except Exception as e:
            raise


if __name__ == '__main__':
    url_long = "https://rbh-tools.ru/catalog/tokarnyy_instrument/otreznye_kanavochnye_derzhavki/derzhavka_dlya_tocheniya_tortsevoy_kanavki_dgfr/derzhavka_rbh_dgfr_25_100_3t20_/"
    try:
        obj = UrlShortenTinyurl()
        obj.shorten(url_long)
    except Exception as e:
        traceback.print_exc()