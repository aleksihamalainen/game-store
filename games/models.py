from django.db import models
from django.core.validators import MinValueValidator

class Game(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)])
    description = models.TextField()
    url = models.URLField(default = '', max_length = 200)
    developer = models.ForeignKey('users.Developer', on_delete = models.CASCADE, related_name = 'games')

class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey('users.Account', on_delete = models.CASCADE)
    game = models.ForeignKey('Game', on_delete = models.CASCADE)

class Transaction(models.Model):
    user = models.ForeignKey('users.Account', on_delete = models.CASCADE)
    game = models.ForeignKey('Game', on_delete = models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
