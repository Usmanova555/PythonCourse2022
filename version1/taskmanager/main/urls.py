from django.conf.urls.static import static
from django.urls import path, include
from taskmanager import settings
from .views import pageNotFound
from . import views

# смотрим при переходе на какую страницу и вызываем функцию из views.
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='menu'),
    path('', include('loginsys.urls')),
    path('', include('loginsys.urls')),
    path('profil', views.profil, name='profil'),
    path('forum', views.forum, name='forum'),
    path('createforum', views.createforum, name='createforum'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound

