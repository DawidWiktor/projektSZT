from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')  # to samo co request.POST['username']
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        #  sprawdzenie czy haslo pasuje do uzytkownika
        if user is not None:
            login(request, user)
        else:
            messages.error(request, 'Błędny login lub hasło.')
    return redirect('main_app:start_page')  # bez wzgledu na wynik logowania przekirowanie do glownej


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # haslo w bazie zapisywane jest w formacie <algorithm>$<iterations>$<salt>$<hash> i używa PBKDF2
        # https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-PASSWORD_HASHERS

        # sprawdzenie czy uzytkownik o podanym 'username' juz istnieje
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Użytkownik o podanej nazwie już istnieje.')
            return redirect('main_app:start_page')  # juz taki username istnieje

        new_user = User.objects.create_user(username, email, password, is_active=False)
        new_user.save()

        messages.info(request,'Kliknij w link aktywacyjny wysłany na podany adres e-mail.')
    return redirect('main_app:start_page')

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('main_app:start_page')