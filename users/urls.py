from django.conf.urls import url
from .views import login, register

urlpatterns = [
    url('login', login, name = 'login'),
    url('register', register, name = 'register'),
]