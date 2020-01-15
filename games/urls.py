from django.conf.urls import url
from .views import list_games

urlpatterns = [
    url('games', list_games, name = 'games'),
]