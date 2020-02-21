# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.forms import ModelForm
from .models import Game

# Forms for game adding and editing

class AddGameForm(ModelForm):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 1000, required = False, widget = forms.Textarea())
    price = forms.DecimalField(max_digits = 10, decimal_places = 2)
    url = forms.URLField(label = 'Game url', required = True)
    tags = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Separate\ntags\nby\nnewlines'}), required = False)
    
    class Meta:
        model = Game
        fields = ('title', 'description', 'price', 'url', 'tags')

class DeleteGameForm(ModelForm):

    class Meta:
        model = Game
        fields = ()

class EditGameForm(ModelForm):
    description = forms.CharField(max_length = 1000, required = False, widget=forms.Textarea)
    tags = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Separate\ntags\nby\nnewlines'}), required = False)

    class Meta:
        model = Game
        fields = ('title', 'description', 'price', 'url', 'tags')

class SearchGamesForm(forms.Form):
    
    search_title = forms.CharField(max_length = 1000, required = False)
    search_terms = forms.CharField(max_length = 1000, required = False, widget = forms.TextInput(attrs={'placeholder': 'Eg. Puzzle Rpg'}))

    class Meta:
        model = Game
        fields = ('search_terms','search_title')
