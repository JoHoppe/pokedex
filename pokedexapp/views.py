from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from pokedexapp.models import Pokemon, Sprite
import base64
from . utils.str_types import get_str_types

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
    try:
        pokemon=Pokemon.objects.get(id=id)
        image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
        pokemon.sprite.image_data_base64 = image_data_base64
        str_types=get_str_types(pokemon.get_type())
        print(str_types,pokemon.get_type())

        if id>1 :
            prev_pokemon=Pokemon.objects.get(id=id-1)
            prev_pokemon.sprite.image_data_base64 = base64.b64encode(prev_pokemon.sprite.image).decode('utf-8') if prev_pokemon.sprite and prev_pokemon.sprite.image else None

        else:
            prev_pokemon=Pokemon()

        if Pokemon.objects.count()<=id :
            next_pokemon = Pokemon()

        else:
            next_pokemon = Pokemon.objects.get(id=id + 1)
            next_pokemon.sprite.image_data_base64 = base64.b64encode(next_pokemon.sprite.image).decode(
                'utf-8') if next_pokemon.sprite and next_pokemon.sprite.image else None

        context = {"pokemon": pokemon,"str_types":str_types,"next_pokemon":next_pokemon,"prev_pokemon":prev_pokemon}
        return render(request, "pokedexapp/pokemon.html", context)
    except (TypeError, Pokemon.DoesNotExist) as e:
        return render(request, "pokedexapp/404.html")

def raise_404(request):
    return render(request,"pokedexapp/404.html")

def search(request):
    query=request.GET.get("q")
    #check if input was a number
    try:
        query=int(query)
        q_pokemons = Pokemon.objects.filter(id__contains=query )
        pokemons=list(q_pokemons)
        for pokemon in pokemons:
            image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
            pokemon.sprite.image_data_base64 = image_data_base64

        context = {"pokemons": pokemons}
        return render(request, "pokedexapp/search.html", context, )

    except ValueError:
        q_pokemons=Pokemon.objects.filter(name__contains=query)
        pokemons = list(q_pokemons)
        if len(pokemons)>=1:
            for pokemon in pokemons:
                image_data_base64 = base64.b64encode(pokemon.sprite.image).decode('utf-8')
                pokemon.sprite.image_data_base64 = image_data_base64


            context = {"pokemons": pokemons}
            return render(request, "pokedexapp/search.html", context, )
        else:
            return render(request,"pokedexapp/404.html")


