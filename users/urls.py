from django.conf.urls import url
from .views import login_view, register, profile, logout_view

urlpatterns = [
    url('login', login_view, name = 'login'),
	url('logout', logout_view, name = 'logout'),
    url('register', register, name = 'register'),
	url('profile', profile, name = 'profile')	
]
