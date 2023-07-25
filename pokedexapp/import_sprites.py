from pokedexapp.models import Pokemon, Sprite
import os

def import_sprites():
    basepath = "C:/Users/jhoho/PycharmProjects/pk_downloader/pokemon_sprites/"
    for number in range(1, 152):
        pokemon_id = str(number).zfill(3)
        filepath = os.path.join(basepath, f"{pokemon_id}.png")

        try:
            with open(filepath, 'rb') as file:
                # Get or create the Sprite instance for the Pokemon
                sprite, created = Sprite.objects.get_or_create(pokemon__id=pokemon_id)
                # Save the sprite image to the 'image' field of the Sprite instance
                sprite.image.save(f"{pokemon_id}.png", file, save=True)
                print(f"Sprite for Pokemon {pokemon_id} imported successfully.")
        except FileNotFoundError:
            print(f"Sprite for Pokemon {pokemon_id} not found.")
        except Exception as e:
            print(f"Error importing sprite for Pokemon {pokemon_id}: {e}")
