import base64

from django.shortcuts import render, get_object_or_404

from pokedexapp.models import Pokemon
from .utils.util_type import get_str_type

from users import views as uviews

# Create your views here.
def index(request):
    pokemons = show_all_pokemon(request)

    # Encode the image data of sprites to base64
    for pokemon in pokemons:
        pokemon.type_name = get_str_type(pokemon.get_type())
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
    if id > total_pokemons or id <= 0:
        return render(request, "pokedexapp/404.html")

    # Get the current and adjacent Pokemon
    pokemon = get_object_or_404(Pokemon, id=id)

    prev_id = id - 1
    next_id = id + 1

    # If the previous ID is 0, set it to the ID of the last Pokemon
    if prev_id == 0:
        prev_id = total_pokemons

    # If the next ID exceeds the total number of Pokemon, set it to the first Pokemon
    if next_id > total_pokemons:
        next_id = 1

    prev_pokemon = get_object_or_404(Pokemon, id=prev_id)
    next_pokemon = get_object_or_404(Pokemon, id=next_id)

    # Encode the image data of the sprite to base64
    encode_poke_sprite(pokemon)

    prev_pokemon.sprite.image_data_base64 = base64.b64encode(prev_pokemon.sprite.image).decode('utf-8')
    next_pokemon.sprite.image_data_base64 = base64.b64encode(next_pokemon.sprite.image).decode('utf-8')

    pokemon.type_name = get_str_type(pokemon.get_type())
    pokemon.type_name = list(pokemon.type_name)

    context = {
        "pokemon": pokemon,
        "next_pokemon": next_pokemon,
        "prev_pokemon": prev_pokemon,
    }
    return render(request, "pokedexapp/pokemon.html", context)


def encode_poke_sprite(pokemon):
    image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
    pokemon.sprite.image_data_base64 = image_data_base64


def search(request):
    query = request.GET.get("q")
    if not query:
        # Handle the case where 'q' parameter is empty or not provided
        return render(request, "pokedexapp/404.html")
    # Check if input was a number,
    try:
        query = int(query)
        q_pokemons = Pokemon.objects.filter(id__contains=query)
        # Convert query into a list and iterate over it
        pokemons = list(q_pokemons)
        if len(pokemons) <= 0:
            return render(request,"pokedexapp/404.html")
        else:
            for pokemon in pokemons:
                encode_poke_sprite(pokemon)

            context = {"pokemons": pokemons}

            return render(request, "pokedexapp/search.html", context)

    except (ValueError,TypeError):
        q_pokemons = Pokemon.objects.filter(name__contains=query)
        pokemons = list(q_pokemons)
        # If there are results, we return them; otherwise, we render the 404 page
        if len(pokemons) >= 1:
            for pokemon in pokemons:
                encode_poke_sprite(pokemon)
            context = {"pokemons": pokemons}
            return render(request, "pokedexapp/search.html", context)
        else:
            return render(request, "pokedexapp/404.html")


def raise_404(request):
    return render(request, "pokedexapp/404.html")
