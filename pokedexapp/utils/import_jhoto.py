import csv
from pokedexapp.models import Pokemon

def import_jhoto_pokemon():
    filepath_pokemon = r"G:\YProgramms\PycharmProjects\pokedex\csv_files\pokemonjhoto.csv"
    with open(filepath_pokemon, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            try:
                pokemon = Pokemon.objects.get(id=row['id'])
            except Pokemon.DoesNotExist:
                # If the Pokémon doesn't exist, create a new one
                pokemon = Pokemon(name=row['identifier'], id=row['id'])
                pokemon.save()

    filepath_types = r"G:\YProgramms\PycharmProjects\pokedex\csv_files\jhoto_types.csv"
    with open(filepath_types, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            pokemon = Pokemon.objects.get(id=row['pokemon_id'])
            # Split the types and check for duplicates before updating
            types = set(pokemon.type.split(',')) if pokemon.type else set()
            new_type = row['type_id']
            if new_type not in types:
                types.add(new_type)
                pokemon.type = ','.join(types)
                pokemon.save()

