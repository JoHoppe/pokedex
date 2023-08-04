from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# we use djangos built in user model, has everythin we need
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms.log_reg_form import LoginForm, RegisterForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('pokedexapp:index')  # Redirect to your desired page
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Redirect to a success page or login page
            return redirect('users:login')  # Replace with the appropriate URL
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def my_profile(request):
    return (request, "users/my_profile.html")
