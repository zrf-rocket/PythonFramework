from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib import auth
from .forms import RegistrationForm, LoginForm, ProfileForm, PwdChangeForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form':form})

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form':form})