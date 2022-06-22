""" Создаю views для работы регистрации и авторизации.

Данный функционал я отнесла в другую папку, потому что так он не потеряется и так с ним легче работать."""

# импортирование для работы с запросами отправки-получения данных
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
# csrf-токен для получения данных
from django.template.context_processors import csrf


def login(request):
    """ Функция авторизации """
    args = {}
    args.update(csrf(request))
    # запрос на ввод пользователем данных
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password = password)
        if user is not None:
            auth.login(request, user)
            # возвращение на главную страницу после авторизации
            return redirect('forum')
        else:
            args['login_error'] = "User is not found"
    # отправка данных, непосредственно, на страницу логина (Войти)
    return render(request, 'login.html', args)


def logout(request):
    """ Данная функция нужна чтобы выйти со своего аккаунта """
    auth.logout(request)
    return redirect("forum")


def register(request):
    """ Функция регистрации """
    args = {}
    # csrf-токен получения данных при регистрации
    args.update(csrf(request))
    # использование формы из библиотеки auth для регистрации
    args['form'] = UserCreationForm()
    # ввод данных в форму
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        # сохранение данных пользователя
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'], password=newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
            # возвращение после регистрации на страницу главная
            return redirect('forum')
        else:
            args['form'] = newuser_form
    # отправка данных регистрации на страницу для работы с ней через html
    return render(request, 'register.html', {"form": args['form']})



