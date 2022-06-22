""" Views представляют собой хранимый запрос к базе данных

они работают с формами и моделями. Отправляют именно те данные на страницы, которые должны на них
отобразиться. """

from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . import code
from .code import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.views.generic import TemplateView
# для проверки авторизации
from django.contrib import auth


def forum(request):
    forums = Forum.objects.order_by('-id')[:1]
    return render(request, 'main/forum.html', {'title': 'Главная страница', 'forums': forums, 'a': code.shorten(), 'username': auth.get_user(request).username})


# При нажатии на кнопку "Сократить", данные отправляются на через эту вьюшку POST-запросом
def createforum(request):
    """ Функция для отправки формы, в которую пользователь вставляет ссылку """
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')
        else:
            error = 'error'
    form = ForumForm()
    # context передаст на форму заполнения формы эти параметры
    context = {
        'form': form,
        'error': error,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/createforum.html', context)


def profil(request):
    """ Функция для заполнения страницы профиля пользователя """
    info = Profile.objects.all()[:1]
    # для отображения ссылок на странице пользователя (по заданному мною фильтру они будут идти в порядке убывания)
    lls = Forum.objects.order_by('-id')
    # это уже нужно для использования данных на странице html
    return render(request, 'main/profil.html', {'title': 'All Links', 'info':info, 'lls':lls})


def pageNotFound(request, exception):
    """ Функция для корректного отображения ошибки """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
