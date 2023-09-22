# pokedexapp/context_processors.py
#make the forms avaible for the base html, therefore everywhere
from users.forms.log_reg_form import LoginForm,RegisterForm


def custom_forms(request):
     forms={"log_form":LoginForm,"reg_form":RegisterForm}
     return forms