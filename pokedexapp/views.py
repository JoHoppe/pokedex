from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,Http404
from pokedexapp.models import Pokemon, Sprite
import base64
from . utils.util_type import get_str_type

# Create your views here.
def index(request):
    pokemons = show_all_pokemon(request)

    # Encode the image data of sprites to base64
    for pokemon in pokemons:
        pokemon.type_name= get_str_type(pokemon.get_type())
        pokemon.type_name = list(pokemon.type_name)
        if pokemon.sprite and pokemon.sprite.image:
            image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
            pokemon.sprite.image_data_base64 = image_data_base64

    context = {"pokemons": pokemons}
    return render(request, "pokedexapp/index.html", context)


def show_all_pokemon(request):
    pokemons = Pokemon.objects.all().order_by('id')
    return pokemons

def show_one_pokemon(request, id):
    # Ensure the ID is a positive integer
    try:
        id = int(id)
        if id <= 0:
            return render(request, "pokedexapp/404.html")
    except ValueError:
        return render(request, "pokedexapp/404.html")

    # Get the total number of Pokémon in the database
    total_pokemons = Pokemon.objects.count()
    if id > total_pokemons:
        return render(request, "pokedexapp/404.html")

    pokemon = get_object_or_404(Pokemon, id=id)

    # Encode the image data of the sprite to base64 if available
    if pokemon.sprite and pokemon.sprite.image:
        image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
        pokemon.sprite.image_data_base64 = image_data_base64
    else:
        pokemon.sprite.image_data_base64 = None

    prev_pokemon = get_object_or_404(Pokemon, id=id - 1) if id > 1 else None
    next_pokemon = get_object_or_404(Pokemon, id=id + 1) if id < total_pokemons else None

    if prev_pokemon and prev_pokemon.sprite and prev_pokemon.sprite.image:
        prev_pokemon.sprite.image_data_base64 = base64.b64encode(prev_pokemon.sprite.image).decode('utf-8')
    else:
        prev_pokemon.sprite.image_data_base64 = None

    if next_pokemon and next_pokemon.sprite and next_pokemon.sprite.image:
        next_pokemon.sprite.image_data_base64 = base64.b64encode(next_pokemon.sprite.image).decode('utf-8')
    else:
        next_pokemon.sprite.image_data_base64 = None

    pokemon.type_name = get_str_type(pokemon.get_type())
    pokemon.type_name = list(pokemon.type_name)

    context = {
        "pokemon": pokemon,
        "next_pokemon": next_pokemon,
        "prev_pokemon": prev_pokemon,
    }
    return render(request, "pokedexapp/pokemon.html", context)


def search(request):
    query = request.GET.get("q")
    # Check if input was a number,
    try:
        query = int(query)
        q_pokemons = Pokemon.objects.filter(id__contains=query)
        # Convert query into a list and iterate over it
        pokemons = list(q_pokemons)
        for pokemon in pokemons:
            image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
            pokemon.sprite.image_data_base64 = image_data_base64

        context = {"pokemons": pokemons}
        return render(request, "pokedexapp/search.html", context)

    except ValueError:
        q_pokemons = Pokemon.objects.filter(name__contains=query)
        pokemons = list(q_pokemons)
        # If there are results, we return them; otherwise, we render the 404 page
        if len(pokemons) >= 1:
            for pokemon in pokemons:
                image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
                pokemon.sprite.image_data_base64 = image_data_base64

            context = {"pokemons": pokemons}
            return render(request, "pokedexapp/search.html", context)
        else:
            return render(request, "pokedexapp/404.html")

def raise_404(request):
    return render(request, "pokedexapp/404.html")
