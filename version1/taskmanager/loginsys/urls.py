from django.conf.urls.static import static
from django.urls import path, include
from . import views

# смотрим при переходе на какую страницу и вызываем функцию из views.
from django.urls import path, include

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register')

    # здесь пропишем переход пользователя на страницы
]
