# Использование файла - сделать свой подкласс AppConfig'а, а затем делать импорты уже остальных файлов
from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Сайт для сокращения ссылок'