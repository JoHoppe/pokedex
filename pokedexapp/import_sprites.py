from pokedexapp.models import Pokemon, Sprite
import os

def import_sprites():
    basepath = "C:/Users/jhoho/PycharmProjects/pk_downloader/pokemon_sprites/"
    for number in range(1, 152):
        pokemon_id = str(number).zfill(3)
        filepath = os.path.join(basepath, f"{pokemon_id}.png")
        print(pokemon_id)

        try:
            with open(filepath, 'rb') as file:
                pokemon = Pokemon.objects.get(id=number)
                sprite, created = Sprite.objects.get_or_create(pokemon=pokemon)
                sprite.image=bytes(file.read())
                # Save the sprite image to the 'image' field of the Sprite instance
                sprite.save()
                print(f"Sprite for Pokemon {pokemon_id} imported successfully.")

        except FileNotFoundError:
            print(f"Sprite for Pokemon {pokemon_id} not found.")
        except Exception as e:
            print(f"Error importing sprite for Pokemon {pokemon_id}: {e}")
