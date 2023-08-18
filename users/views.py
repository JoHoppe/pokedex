import base64
from django.db import IntegrityError

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# we use djangos built in user model, has everythin we need
from django.contrib.auth.views import LogoutView
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from trainercard.models import TrainerCard
from .forms.log_reg_form import LoginForm, RegisterForm


# Create your views here.

def custom_login(request):
    error_messages = []

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
                error_messages.append("Invalid Username, Email or Password.")
                return render(request, "users/login.html", {"log_form": form, "error_messages": error_messages})
        else:
            error_messages.append("Invalid Form")
            return render(request, "users/login.html", {"log_form": form, "error_messages": error_messages})

    else:
        # request was not POST or form is invalid
        form = LoginForm()

    return render(request, "users/login.html", {"log_form": form, "error_messages": error_messages})

def custom_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                # Create the user
                user = User.objects.create_user(username=username, email=email, password=password)
                trainercard = TrainerCard.objects.create(user=user)

                # Redirect to a success page or custom_login page
                return redirect('users:login')
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    if 'username' in str(e):
                        form.add_error('username', "A user with the same username already exists.")
                    elif 'email' in str(e):
                        form.add_error('email', "A user with the same email already exists.")
                else:
                    form.add_error(None, "An error occurred during registration.")
        else:
            # Form is invalid, render the registration form with errors
            return render(request, 'users/register.html', {'form': form})

    else:
        # GET request, render the registration form
        form = RegisterForm()

    return render(request, 'users/register.html', {'form': form})


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('pokedexapp:index')  # Redirect to the login page


@login_required
def profile(request, username):
    try:
        profile = User.objects.get(username=username)
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)

    user = request.user
    is_owner = user == profile

    try:
        trainercarduser = TrainerCard.objects.get(user=user)
    except TrainerCard.DoesNotExist:
        return HttpResponse("TrainerCard not found", status=404)

    try:
        trainercard = TrainerCard.objects.get(user=profile)
        image_data_base64 = base64.b64encode(trainercard.fav_pokemon.sprite.image).decode('utf-8')
        trainercard.fav_pokemon.sprite.image_data_base64 = image_data_base64
    except TrainerCard.DoesNotExist:

        return HttpResponse("TrainerCard not found for profile user", status=404)

    context = {"trainercard": trainercard, "is_owner": is_owner}
    return render(request, "users/profile.html", context)


def edit_profile(request):
    pass
