from django.urls import path
from .views import list_games, purchase_game, view_game

urlpatterns = [
    path('games/all/', list_games, name = 'games'),
    path('games/<int:game_id>/', view_game, name = 'view_game'),
    path('purchase/<int:game_id>/', purchase_game, name = 'purchase_game')
]