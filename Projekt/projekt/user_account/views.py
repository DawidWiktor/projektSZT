from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Wrong login or password.')
    return redirect('main_app:start_page')  


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Login exists.')
            return redirect('main_app:start_page')

        new_user = User.objects.create_user(username, email, password, is_active=False)
        new_user.save()
    return redirect('main_app:start_page')

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('main_app:start_page')