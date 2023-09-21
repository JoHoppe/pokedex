from django import forms
from trainercard.models import TrainerCard


class Profile_pic_form(forms.ModelForm):
    class Meta:
        model = TrainerCard
        fields = ["profile_pic"]
