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

from django.contrib import auth


def forum(request):
    forums = Forum.objects.order_by('-id')[:1]
    return render(request, 'main/forum.html', {'title': 'Страница с отзывами', 'forums': forums, 'a': code.shorten(), 'username': auth.get_user(request).username})


def createforum(request):
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forum')
        else:
            error = 'error'
    form = ForumForm()
    context = {
        'form': form,
        'error': error,
        'username': auth.get_user(request).username
    }
    return render(request, 'main/createforum.html', context)


def profil(request):
    info = Profile.objects.all()[:1]
    lls = Forum.objects.order_by('-id')[:5]
    return render(request, 'main/profil.html', {'title': 'Профиль пользователя', 'info':info, 'lls':lls})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
