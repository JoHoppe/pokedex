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
    pokemon = models.OneToOneField(Pokemon, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="pokemon_sprites")