from __future__ import unicode_literals
from .forms import RegistrationForm, LoginForm, EditProfileForm
from .models import Developer, Player
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
	return render(request, './profile.html', {'user': request.user})

def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')
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
	
@login_required
def edit_profile_view(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
		else:
			form = EditProfileForm(instance = request.user)
			return render(request, 'edit_profile.html', {'form': form})	
	else:
		form = EditProfileForm(instance = request.user)
		return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile_view(request):
	return redirect('profile')

def logout_view(request):
	logout(request)
	return redirect('index')

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			acc = form.save()
			acc_type = form.cleaned_data['account_type']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			acc_id = acc.id
			if acc_type == 'DEV':
				developer = Developer(user_id = acc_id)
				developer.save()
			else:
				player = Player(user_id = acc_id)
				player.save()
			user = authenticate(request, username = username, password = password)
			login(request, user)
			return redirect('profile')
	else:
		form = RegistrationForm()
		return render(request, './register.html', {'form' : form})