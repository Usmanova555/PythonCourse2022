""" models отвечают за то, чтобы создавать миграции для баз данных

Они состоят из составляющих класса в models.
Например, у пользователя на сайте будут данные о его ФИО и email. Больше никаких данных не будет, но если я добавлю
новых, что-то удалю или свяжу профиль с помощью many to many с каким-нибудь новым функционалом, то у него будет
ещё и это. То есть одна модель содержит всю информацию о своём объекте для работы с базами данных в формах и вьюшках """

from django.contrib.auth.models import AbstractUser
from django.db import models


def __str__(self):
    """ Очень нужная функция для отображения названия страниц на сайте """
    return self.title


class Profile(models.Model):
    """ Данные пользователя """
    name = models.CharField(max_length=50, verbose_name="Имя")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")
    email = models.EmailField(verbose_name="Email")

    class Meta:
        """ Данный класс отобразит понятное название модели уже в панели администратора """
        verbose_name_plural = 'Профили пользователей'


class Forum(models.Model):
    """ Данные формы для ссылки """
    message = models.TextField(verbose_name="Текст ссылки")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания сокращённой ссылки")

    class Meta:
        verbose_name_plural = 'Ссылки'
        ordering = ['created']