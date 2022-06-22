import requests
import sys
import traceback
import urllib
from .views import *
from .forms import *


def shorten():
    url_long = Forum.message
    URL = "http://tinyurl.com/api-create.php"
    try:
        url = URL + "?" \
            + urllib.parse.urlencode({"url": url_long})
        res = requests.get(url)
        effect = res.text


    except Exception as e:
        raise
