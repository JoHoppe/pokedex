from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models

from pokedexapp.models import Pokemon



class TrainerCard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #blank,so no input required in form
    #TODO:set Default
    profile_pic = models.ImageField(null=True,blank=True,upload_to="media/profilepics")
    fav_pokemon = models.ForeignKey(Pokemon, on_delete=models.SET_NULL, null=True, default=1)


    def set_fav_pokemon(self, new_fav_pokemon):
        self.fav_pokemon = new_fav_pokemon
        self.save()

    def __str__(self):
        return self.user.username
    def set_profile_pic(self,new_profile_pic):
        self.profile_pic=new_profile_pic
        self.save()

    def get_profile_pic(self):
        return self.profile_pic
        #TODO: implement set profile pic
