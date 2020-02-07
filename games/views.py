from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Game
from users.models import Developer
from .forms import AddGameForm

def list_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})


def add_game(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('./no_profile.html')
    if user.account_type != 'DEV':
        return HttpResponse('<p>You are a player</p>')
    if request.method == 'POST':
        form = AddGameForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            url = form.cleaned_data['url']
            dev = Developer.objects.get(user_id = user.id)
            game = Game(
                title = title,
                description = description,
                price = price,
                url = url,
                developer = dev)
            game.save()
            return redirect('games')
    else:
        form = AddGameForm()
        return render(request, './add_game_form.html', {'form': form})