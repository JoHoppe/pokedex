import os
import requests
from django.conf import settings
from pokedexapp.models import Pokemon, Sprite


def import_sprites():
    base_url = "https://assets.pokemon.com/assets/cms2/img/pokedex/full/"
    basepath = "G:/YProgramms/PycharmProjects/pokedex/jhoto_sprites"

    for number in range(151, 252):  # Update the range to 151-251
        pokemon_id = str(number).zfill(3)
        filepath = os.path.join(basepath, f"{pokemon_id}.png")
        print(f"Importing sprite for Pokémon {pokemon_id}")

        try:
            # Download the sprite image from the web
            sprite_url = f"{base_url}{number}.png"
            response = requests.get(sprite_url)

            if response.status_code == 200:
                with open(filepath, 'wb') as file:
                    file.write(response.content)

                # Now you can proceed to save it to the database
                with open(filepath, 'rb') as file:
                    pokemon = Pokemon.objects.get(id=number)
                    sprite, created = Sprite.objects.get_or_create(pokemon=pokemon)
                    sprite.image = bytes(file.read())
                    sprite.save()
                    print(f"Sprite for Pokémon {pokemon_id} imported and saved successfully.")
            else:
                print(f"Failed to download sprite for Pokémon {pokemon_id}")

        except Exception as e:
            print(f"Error importing sprite for Pokémon {pokemon_id}: {e}")


if __name__ == "__main__":
    # Call the import_sprites function when the script is executed
    import_sprites()
