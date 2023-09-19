from django import forms




class Profile_pic_form(forms.Form):
    profile_pic_form = forms.ImageField(required=True,label="Upload a Profile Picture",)




