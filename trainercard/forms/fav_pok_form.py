from django import forms
from pokedexapp.models import Pokemon


class Fav_pok_form(forms.Form):
    fav_pok = forms.CharField(label="Display your favorite Pokemon", required=False)
    fav_pok.widget.attrs['placeholder'] = 'eg.: "12" or "Abra"'
    def clean_fav_pok(self):
        fav_pok = self.cleaned_data.get('fav_pok')

        try:
            fav_pok_id = int(fav_pok)
            pokemon_obj = Pokemon.objects.get(id=fav_pok_id)
            fav_pok = pokemon_obj.id
        except (ValueError, Pokemon.DoesNotExist):
            fav_pok_form = fav_pok.lower().strip()
            try:
                pokemon_obj = Pokemon.objects.get(name=fav_pok_form)
                fav_pok = pokemon_obj.id
            except Pokemon.DoesNotExist:
                raise forms.ValidationError("Input is not a valid Pokemon ID or Name")
        return fav_pok

