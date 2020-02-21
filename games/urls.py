from django.urls import path
from .views import list_games, purchase_game, view_game, add_game, payment, delete_game, edit_game, play_game, score_list, submit_score, save_game, load_game

urlpatterns = [
    path('games/all/', list_games, name = 'games'),
    path('games/<int:game_id>/', view_game, name = 'view_game'),
    path('games/purchase/<int:game_id>/', purchase_game, name = 'purchase_game'),
    path('games/delete/<int:game_id>/', delete_game, name='delete_game'),
    path('games/edit/<int:game_id>/', edit_game, name = 'edit_game'),
    path('games/play/<int:game_id>/', play_game, name = 'play_game'),
    path('games/score/<int:game_id>/', score_list, name = 'score'),
    path('games/submit_score/<int:game_id>/', submit_score, name = 'submit_score'),
    path('games/save_game/<int:game_id>/', save_game, name = 'save_game'),
    path('games/load_game/<int:game_id>/', load_game, name = 'load_game'),
    path('games/add/', add_game, name = 'add_game'),
    path('payment/<int:game_id>/<str:status>/', payment, name = 'payment')
]