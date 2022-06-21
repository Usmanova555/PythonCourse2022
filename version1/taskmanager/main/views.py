from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.views.generic import TemplateView

from django.contrib import auth


def index(request):
    return render(request, 'main/index.html')
    # путь к шаблону - как будто я уже в папке templates


def forum(request):
    forums = Forum.objects.order_by('-id')[:10]
    return render(request, 'main/index.html', {'title': 'Страница для ссылок', 'forums': forums, 'username': auth.get_user(request).username})


def createforum(request):
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'error'
    form = ForumForm()
    context = {
        'form': form,
        'error': error,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/index.html', context)


def profil(request):
    info = Profile.objects.all()[:1]
    return render(request, 'main/profil.html', {'title': 'Профиль пользователя', 'info': info})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
