from django.shortcuts import render, redirect

def index(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    return render(request, 'index.html')
