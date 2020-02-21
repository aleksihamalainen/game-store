from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, JsonResponse
from .models import Game, Score, Transaction, GameState
from users.models import Developer, Account
from .forms import AddGameForm, DeleteGameForm, EditGameForm
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
            transactions = Transaction.objects.filter(game = game)
            return render(request, 'game_dev.html', {'game': game, 'transactions': transactions})
        else:
            owns_game = user.owned_games.filter(pk=game_id).count() != 0
            return render(request, 'game.html', {'game': game, 'owns_game': owns_game})
    return render(request, 'game.html', {'game': game})

@login_required
def edit_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if user.id == game.developer.user_id:
        if request.method == 'POST':
            form = EditGameForm(request.POST, instance = game)
            if form.is_valid():
                form.save()
                return redirect(f'/games/{game.id}/')
        else:
            form = EditGameForm(instance = game)
            return render(request, 'edit_game.html', {'form': form, 'game': game})
    else:
        raise PermissionDenied()

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
            return render(request, 'delete_game.html', {'form': form, 'game': game})
    else:
        raise PermissionDenied()


@login_required
def play_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if user.owned_games.filter(pk=game_id).count() != 0 or user.id == game.developer.user_id:
        scores = Score.objects.filter(game_id = game_id).order_by('-score')
        return render(request, 'play_game.html', {'game' : game, 'scores': scores})
    else:
        raise PermissionDenied()

@login_required
def score_list(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if user.owned_games.filter(pk=game_id).count() != 0 or user.id == game.developer.user_id:
        scores = Score.objects.filter(game_id = game_id).order_by('-score')
        return render(request, 'score_list.html', {'scores': scores, 'game': game})
    else:
        raise PermissionDenied()

@login_required
def submit_score(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if user.owned_games.filter(pk=game_id).count() != 0 or user.id == game.developer.user_id:
        new_score = request.GET['score']
        try:
            prev_score = Score.objects.get(game_id = game_id, user_id = user.id)
        except:
            score = Score()
            score.score = new_score
            score.user = user
            score.game = game
            score.save()
            return HttpResponse('success')
        if prev_score.score >= int(new_score):
            return HttpResponse('fail')
        else:
            prev_score.score = new_score
            prev_score.save()
            return HttpResponse('success')
    else:
        return HttpResponse('fail')

@login_required
def save_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    if user is None:
        return HttpResponse('fail')
    if user.owned_games.filter(pk=game_id).count() != 0 or user.id == game.developer.user_id:
        new_save = request.GET['gameState']
        try:
            gamestate = GameState.objects.get(game_id = game_id, user_id = user.id)
            gamestate.state = new_save
        except:
            gamestate = GameState(state = new_save, user = user, game = game)    
        gamestate.save()
        return HttpResponse('success')
            
    else:
        return HttpResponse('fail')

@login_required
def load_game(request, game_id):
    user = request.user
    game = get_object_or_404(Game, id = game_id)
    state = get_object_or_404(GameState, game_id = game_id, user_id = user.id)
    return HttpResponse(state.state)

@login_required
def purchase_game(request, game_id):
    game = get_object_or_404(Game, id = game_id)
    user = request.user
    if user.owned_games.filter(pk=game_id).count() != 0 or user.id == game.developer.user_id:
        return redirect(f'/games/{game.id}/')
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
        transaction = Transaction(user = user, game = game, price = game.price)
        user.owned_games.add(game)
        transaction.save()
        user.save()
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
