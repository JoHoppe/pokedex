from django.contrib.auth.models import User
from django.db import models

from pokedexapp.models import Pokemon


class TrainerCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #blank,so no input required in form
    profile_pic = models.ImageField(null=True,blank=True)
    fav_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, default=1)


    def set_fav_pokemon(self, new_fav_pokemon):
        self.fav_pokemon = new_fav_pokemon
        self.save()

    def set_profile_pic(self):
        pass
        #TODO: implement set profile pic