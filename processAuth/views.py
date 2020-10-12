from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def authentication(request):

    if request.user.is_authenticated:
        return redirect('client_list')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:

        login(request, user)
        return redirect('client_list')

    else:
        messages.error(request, 'Usuario o contraseña invalidos.')

    return render(request, 'auth/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('authentication')
