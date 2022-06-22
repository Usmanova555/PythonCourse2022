from django.conf.urls.static import static
from django.urls import path, include
from taskmanager import settings
from .views import pageNotFound
from . import views

# смотрим при переходе на какую страницу и вызываем функцию из views.
from django.urls import path, include

urlpatterns = [
    path('', include('loginsys.urls')),
    path('', include('loginsys.urls')),
    path('createforum', views.createforum, name='createforum'),
    path('profil', views.profil, name='profil'),
    path('', views.forum, name='forum')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

