""" Файл admin.py необходим чтобы зарегистрировать пользователя и ссылки, с которыми он работает на странице forum.

Таким образом, администратор может видеть данные любых пользователей в панели администратора, а так же
работать с ними. Так же в панели администратора админ может выбирать любому пользователю права доступа,
добавлять различную информацию из файла model, такую как ФИО, email и т.д. """

from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import *

admin.site.register(Profile)
admin.site.register(Forum)
