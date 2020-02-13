from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .models import Game
from users.models import Developer, Account
from .forms import AddGameForm, DeleteGameForm
from django.contrib.auth.decorators import login_required
from hashlib import md5

def list_games(request):
    games = Game.objects.all()
    return render(request, 'games.html', {'games': games})

def view_game(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    user = request.user
    if user.is_authenticated:
        if user.id == game.developer.user_id:
            return render(request, 'game_dev.html', {'game': game})
        else:
            return render(request, 'game.html', {'game': game})
    return render(request, 'game.html', {'game': game})

@login_required
def delete_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    developer_id = game.developer.user_id
    if user.id == developer_id:
        if request.method == 'POST':
            game.delete()
            return redirect('games')
        else:
            form = DeleteGameForm()
            return render(request, 'delete_game.html', {'form': form})
    else:
        raise PermissionDenied()

@login_required
def purchase_game(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    sid = "azLMOnNlbGxlcg=="
    pid = str(game.id)
    secret = "DbG5kmGnFmWBOh6SsWHRstQYZ7QA"
    checksumstr = f"pid={pid:s}&sid={sid:s}&amount={game.price:.2f}&token={secret:s}"
    checksum = md5(checksumstr.encode('utf-8')).hexdigest()
    return render(request, 'payment.html', {'game': game, 'sid': sid, 'pid': pid, 'checksum': checksum})

@login_required
def payment(request, status, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if status == 'success':
        user.owned_games.add(game)
        return render(request, 'success.html')
    elif status == 'cancel':
        return render(request, 'cancel.html')
    else:
        return render(request, 'error.html')        

@login_required
def add_game(request):
    user = request.user
    if user.account_type != 'DEV':
        raise PermissionDenied()
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
    else:
        form = AddGameForm()
        return render(request, './add_game_form.html', {'form': form})
