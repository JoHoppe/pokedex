from django import forms
from pokedexapp.models import Pokemon

class Fav_pok_form(forms.Form):
    fav_pok_form = forms.CharField(label="Fav_Pok_Form", required=True)


    def clean_fav_pok_form(self):
        fav_pok_form = self.cleaned_data.get('fav_pok_form')

        try:
            fav_pok_id = int(fav_pok_form)
            Pokemon.objects.get(id=fav_pok_id)



        except ValueError:
            fav_pok_form = fav_pok_form.lower().strip()
            try:
                Pokemon.objects.get(name=fav_pok_form)
            except Pokemon.DoesNotExist:
                raise forms.ValidationError("Input is not a valid Pokemon ID or Name")

        return cleaned_deta