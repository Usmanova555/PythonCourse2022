""" Функция формирования и хранения сокращенных ссылок при помощи хэша

Аналог сервиса TinyURL, предусмотрен обход коллизий - Hash Salt. """

import requests
import sys
import traceback
import urllib
from .views import *
from .forms import *


def shorten():
   # беру данные, которые ввёл пользователь (ссылка) и работаю с ней
   url_long = Forum.message
   URL = "http://tinyurl.com/api-create.php"
   try:
       url = URL + "?" \
           + urllib.parse.urlencode({"url": url_long})
       res = requests.get(url)
       effect = res.text

   # корректная обработка ошибки в случае её возникновения
   except Exception as e:
       raise
