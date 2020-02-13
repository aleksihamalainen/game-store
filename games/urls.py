from django.urls import path
from .views import list_games, purchase_game, view_game, add_game, payment

urlpatterns = [
    path('games/all/', list_games, name = 'games'),
    path('games/<int:game_id>/', view_game, name = 'view_game'),
    path('games/purchase/<int:game_id>/', purchase_game, name = 'purchase_game'),
    path('games/add/', add_game, name = 'add_game'),
    path('payment/<int:game_id>/<str:status>/', payment, name = 'payment')
]