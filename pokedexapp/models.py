from django.db import models

# Create your models here.

class Pokemon(models.Model):
    name=models.CharField(max_length=100,null=True)
    type=models.CharField(max_length=2,null=True)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type.split(',') if',' in self.type else [self.type]

    def get_number(self):
        return self.id

class Sprite(models.Model):
    #we use sqlite blob to save the pngs, therefore we need the image to be a binary
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE)
    image = models.BinaryField()

class Utils(models.Model):

    #place for all utilities we might need, like mssinngno sprite
    image = models.BinaryField(null=True)