import os
from django.conf import settings
from pokedexapp.models import Pokemon, Sprite, Utils

# Configure Django settings on-the-fly
settings.configure(
    DEBUG=True,  # Set DEBUG to True or False as needed
    INSTALLED_APPS=[
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.admin',
        'pokedexapp',  # Add the name of your app here
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../db.sqlite3'),
        }
    }
)

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
                sprite.image = bytes(file.read())
                # Save the sprite image to the 'image' field of the Sprite instance
                sprite.save()
                print(f"Sprite for Pokemon {pokemon_id} imported successfully.")

        except FileNotFoundError:
            print(f"Sprite for Pokemon {pokemon_id} not found.")
        except Exception as e:
            print(f"Error importing sprite for Pokemon {pokemon_id}: {e}")

def import_sprite():
    basepath = "C:/Users/jhoho/PycharmProjects/pk_downloader/pokemon_sprites/"
    spritename = input("Spritename without png: ")
    filepath = os.path.join(basepath, f"{spritename}.png")
    try:
        with open(filepath, 'rb') as file:
            util, created = Utils.objects.get_or_create()
            util.image = bytes(file.read())
            # Save the sprite image to the 'image' field of the Utils instance
            util.save()
            print(f"Sprite for Util {util.id} imported successfully.")

    except FileNotFoundError:
        print(f"Sprite for util {spritename} not found.")
    except Exception as e:
        print(f"Error importing sprite for Util {spritename}: {e}")

def main():
    # Call the functions here as needed
    import_sprites()
    import_sprite()

if __name__ == "__main__":
    main()
