from django.contrib import admin
from .models import Game, Score, Transaction

admin.site.register([Game, Score, Transaction])