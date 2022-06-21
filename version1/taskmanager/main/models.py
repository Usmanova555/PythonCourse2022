from django.contrib.auth.models import AbstractUser
from django.db import models


def __str__(self):
    return self.title


class Profile(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    lastname = models.CharField(max_length=50, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=50, verbose_name="Отчество")

    class Meta:
        verbose_name_plural = 'Профили пользователей'


class Forum(models.Model):
    message = models.TextField(verbose_name="Текст ссылки")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Время создания ссылки")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Ссылка'
