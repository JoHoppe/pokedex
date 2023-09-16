from django import forms




class Profile_pic_form():
    profile_pic_form = forms.ImageField(required=True,label="Profile_Pic_Form")

    def clean_profile_pic_form(self):
        profile_pic_form=self.cleaned_data.get('profile_pic_form')
        #Todo: require imagefield to be of right sizhe



