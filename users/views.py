# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import RegistrationForm, LoginForm
from .models import Developer, Player
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def profile(request):
	user = request.user
	if user.is_authenticated:
		return render(request, './profile.html', {'user': user})
	else:
		return render(request, './no_profile.html')

def login_view(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('profile')
		else:
			return redirect('index')
	else:
		form = LoginForm()
		return render(request, './login.html', {'form': form})
	
def logout_view(request):
	logout(request)
	return redirect('index')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			acc = form.save()
			acc_type = form.cleaned_data['account_type']
			acc_id = acc.id
			if(acc_type == 'DEV'):
				developer = Developer(user_id = acc_id)
				developer.save()
			else:
				player = Player(user_id = acc_id)
				player.save()
			return redirect('index')
		return redirect('index')
	else:
		form = RegistrationForm()
		return render(request, './register.html', {'form' : form})
