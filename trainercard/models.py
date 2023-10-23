import os

import PIL
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from trainercard.validator import validate_file_size
from pokedexapp.models import Pokemon

from PIL import Image
import io


def default_profile_pic():
    # Create a white 360x360 image
    image = Image.new('RGB', (360, 360), color='white')
    return image


class PokeTeam(models.Model,):
    team_name=models.CharField(unique=False,max_length=15,default="My first Team")
    pok_1 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_1")
    pok_2 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_2")
    pok_3 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_3")
    pok_4 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_4")
    pok_5 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_5")
    pok_6 = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, related_name="pok_6")


class TrainerCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True,
                                    upload_to="profilepics",
                                    validators=[validate_file_size])

    fav_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, default=1)
    poke_teams = models.OneToOneField(PokeTeam,on_delete=models.CASCADE,null=True)



    def __str__(self):
        return self.user.username




