from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# we use djangos built in user model, has everythin we need
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms.log_reg_form import LoginForm, RegisterForm
from trainercard.models import TrainerCard
from pokedexapp.models import Pokemon
import base64




# Create your views here.


def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username_or_email')
            password = form.cleaned_data.get('password')

            # Attempt authentication with username
            user = authenticate(request=request, username=username_or_email, password=password)

            # If authentication with username fails, attempt with email
            if user is None:
                user = authenticate(request=request, email=username_or_email, password=password)

            if user is not None:
                login(request, user)
                return redirect('pokedexapp:index')  # Redirect to your desired page
        else:
            # Display form errors to the user
            print(form.errors)
    else:
        form = LoginForm()

    return render(request,"", {'form': form})


def custom_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            trainercard=TrainerCard.objects.create(user=user)

            # Redirect to a success page or custom_login page
            return redirect('pokedexapp:index')  # Replace with the appropriate URL
    else:
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('pokedexapp:index')  # Redirect to the login page


@login_required
def my_profile(request):
    user=request.user
    trainercard = TrainerCard.objects.get(user=user)

    image_data_base64 = base64.b64encode(trainercard.fav_pokemon.sprite.image).decode('utf-8')
    trainercard.fav_pokemon.sprite.image_data_base64 = image_data_base64
    context={"trainercard": trainercard,"user":user, }
    return render(request,"users/my_profile.html",context)