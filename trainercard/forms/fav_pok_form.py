from django import forms
from pokedexapp.models import Pokemon

class Fav_pok_form(forms.Form):
    fav_pok = forms.CharField(label="Fav_Pok_Form", required=False)

    def clean(self):
        cleaned_deta = super().clean()
        fav_pok = self.cleaned_data.get('fav_pok')

        try:
            fav_pok_id = int(fav_pok)
            Pokemon.objects.get(id=fav_pok_id)



        except ValueError:
            fav_pok_form = fav_pok.lower().strip()
            try:
                Pokemon.objects.get(name=fav_pok_form)
            except Pokemon.DoesNotExist:
                raise forms.ValidationError("Input is not a valid Pokemon ID or Name")
