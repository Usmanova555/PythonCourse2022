from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.forms import forms


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["message"]
        widgets = {
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст ссылки:'
            })
        }

    def clean_title_f(self):
        message = self.cleaned_data['message']
        if len(message) > 400:
            raise ValidationError('Длина превышает 400 символов')

        return message