from django.shortcuts import render
from django.http import HttpResponse
from .models import Game

def list_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})