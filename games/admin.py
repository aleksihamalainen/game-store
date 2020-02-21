from django.contrib import admin
from .models import Game, Score, Transaction, GameState

admin.site.register([Game, Score, Transaction, GameState])