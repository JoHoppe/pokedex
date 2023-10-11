# pokedexapp/context_processors.py
#make the forms avaible for the base html, therefore everywhere
from users.forms.log_reg_form import LoginForm,RegisterForm
from trainercard.models import TrainerCard


def custom_forms(request):
     forms={"log_form":LoginForm,"reg_form":RegisterForm}
     return forms


def context_trainer_card(request):
    trainercard = None  # Default value if user is not logged in or doesn't have a TrainerCard
    if request.user.is_authenticated:
        try:
            trainercard = TrainerCard.objects.get(user=request.user)
        except TrainerCard.DoesNotExist:
            pass  # TrainerCard not found for the user
    return {'trainercard': trainercard}