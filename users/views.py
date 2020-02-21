from __future__ import unicode_literals
from .forms import RegistrationForm, LoginForm, EditProfileForm, DeleteAccountForm
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import PermissionDenied
from .models import Developer, Player
from games.models import Game, Transaction
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

@login_required
def profile(request):
	user = request.user
	transactions = Transaction.objects.filter(user = user)
	if user.account_type == 'DEV':
		developer = get_object_or_404(Developer, user_id = user.id)
		developed_games = Game.objects.filter(developer = developer.user_id)
		return render(request, 'profile.html', {'user': user, 'transactions': transactions, 'developed_games': developed_games})
	else:
		return render(request, 'profile.html', {'user': user, 'transactions': transactions})

def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			form = LoginForm()
			return render(request, 'login.html', {'form': form, 'errorMessage': 'User does not exist or wrong password!'})
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})

@login_required
def edit_profile_view(request):
	user = request.user
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
		else:
			form = EditProfileForm(instance = request.user)
			return render(request, 'edit_profile.html', {'form': form, 'errorMessage': 'Failed to edit profile!'})

	else:
		form = EditProfileForm(instance = request.user)
		return render(request, 'edit_profile.html', {'form': form})

@login_required
def change_password_view(request):
	user = request.user
	if request.method == 'POST':
		form = PasswordChangeForm(user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request, user)
			return redirect('profile')
		else:
			form = PasswordChangeForm(user)
			return render(request, 'edit_profile.html', {'form': form, 'errorMessage': 'Failed to change password!'})
	else:
		form = PasswordChangeForm(user)
		return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile_view(request):
	if request.method == 'POST':
		request.user.delete()
		return redirect('index')
	else:
		form = DeleteAccountForm()
		return render(request, 'delete_profile.html', {'form': form})

def logout_view(request):
	logout(request)
	return redirect('index')

def verify(request):
	user = request.user
	send_mail(
    'Email verification',
    'Please verify your email',
    'gamestore@gmail.com',
    [user.email],
    fail_silently=False,
	)

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
				verify(developer)
			else:
				player = Player(user_id = acc_id)
				player.save()
				verify(player)
			user = authenticate(request, username = username, password = password)
			login(request, user)
			return redirect('index')
		else:
			return render(request, 'register.html', {'form' : form, 'errorMessage': 'Registration failed!'})
	else:
		form = RegistrationForm()
		return render(request, 'register.html', {'form' : form})