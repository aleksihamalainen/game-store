from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game

def list_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})

def view_game(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    return render(request, 'game.html', {'game': game})

def purchase_game(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    return render(request, 'payment.html', {'game': game})