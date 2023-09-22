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


class TrainerCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True
                                    , upload_to="profilepics"
                                    ,validators=[validate_file_size])

    fav_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, default=1)

    def __str__(self):
        return self.user.username
