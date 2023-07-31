from django.shortcuts import render
from pokedexapp.models import Pokemon, Sprite
import base64


# Create your views here.
def index(request):
    pokemons = show_all_pokemon(request)

    # Encode the image data of sprites to base64 and add it to the context
    for pokemon in pokemons:
        if pokemon.sprite and pokemon.sprite.image:
            image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
            pokemon.sprite.image_data_base64 = image_data_base64

    context = {"pokemons": pokemons}
    return render(request, "pokedexapp/index.html", context)


def show_all_pokemon(request):
    pokemons = Pokemon.objects.all()
    return pokemons


def show_pokemon(request, *ids):
    pokemons = Pokemon.objects.get(*ids)
    for pokemon in pokemons:
        image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
        pokemon.sprite.image_data_base64 = image_data_base64


    context = {"pokemons": pokemons}
    return render(request, "pokedexapp/index.html", context)

def show_one_pokemon(request,id):
    pokemon=Pokemon.objects.get(id=id)
    image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
    pokemon.sprite.image_data_base64 = image_data_base64


    context = {"pokemon": pokemon}
    return render(request, "pokedexapp/pokemon.html", context)