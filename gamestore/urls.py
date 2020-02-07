from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url('', include('games.urls')),
    url('', include('users.urls')),
]