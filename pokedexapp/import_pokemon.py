import csv
from pokedexapp.models import Pokemon

def import_pokemon():
    filepath_pokemon = r"C:\Users\jhoho\PycharmProjects\pokedex\csv_files\pokemon.csv"
    with open(filepath_pokemon, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            pokemon = Pokemon(name=row['identifier'])  # Don't pass the 'id' here.
            pokemon.save()

    filepath_types = r"C:\Users\jhoho\PycharmProjects\pokedex\csv_files\pokemon_types.csv"
    with open(filepath_types, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            pokemon = Pokemon.objects.get(id=row['pokemon_id'])
            if pokemon.type:
                pokemon.type += ',' + row['type_id']
            else:
                pokemon.type = row['type_id']
            pokemon.save()
            #TODO: types as list
