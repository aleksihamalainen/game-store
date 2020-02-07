from django.conf.urls import url
from .views import list_games, add_game

urlpatterns = [
    url('games', list_games, name = 'games'),
    url('add_game', add_game, name = 'add_game')
]