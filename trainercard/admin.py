from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import TrainerCard,PokeTeam

admin.site.register(TrainerCard)
admin.site.register(PokeTeam)
