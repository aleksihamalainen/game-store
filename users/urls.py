from django.conf.urls import url
from django.urls import path
from .views import login_view, register, profile, logout_view, edit_profile_view, delete_profile_view, change_password_view

urlpatterns = [
    url('login', login_view, name = 'login'),
	url('logout', logout_view, name = 'logout'),
    url('register', register, name = 'register'),
	path('profile/', profile, name = 'profile'),
    path('profile/edit', edit_profile_view, name = 'edit'),
    path('profile/edit/change_password', change_password_view, name = 'change_password'),
    path('profile/delete', delete_profile_view, name = 'delete')
]