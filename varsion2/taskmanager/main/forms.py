from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ForumForm(ModelForm):
    class Meta:
        model = Forum
        fields = ["message"]
        widgets = {
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Вставьте ссылку:'
            })
        }
