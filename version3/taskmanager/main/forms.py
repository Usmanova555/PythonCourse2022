""" Данный файл необходим для того, чтобы создавать в нём формы для заполнения на самом сайте пользователем

Форма может содержать числовые, текстовые данные. Данная форма нужна, для того, чтобы в форму на странице
ввода ссылки и нажатия на кнопку сокращения было куда вводить данные. Далее данные передаются в views. """

from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ForumForm(ModelForm):
    """ Создание формы ввода ссылки """
    class Meta:
        model = Forum
        fields = ["message"]
        widgets = {
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вставьте ссылку:'
            })
        }
