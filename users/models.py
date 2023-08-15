from django.contrib.auth.models import User
from django.db import models

from pokedexapp.models import Pokemon

"""
class TrainerCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.BinaryField(null=True)
    fav_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, default=1)


    def set_fav_pokemon(self, new_fav_pokemon):
        self.fav_pokemon = new_fav_pokemon
        self.save()

    def set_profile_pic(self):
        pass"""
