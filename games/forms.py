# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import Game

class AddGameForm(ModelForm):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000, required = False)
    price = forms.DecimalField(max_digits = 10, decimal_places = 2)
    url = forms.URLField(label = 'Game url', required = True)
    
    class Meta:
        model = Game
        fields = ('title', 'description', 'price', 'url')

class DeleteGameForm(ModelForm):

    class Meta:
        model = Game
        fields = ()