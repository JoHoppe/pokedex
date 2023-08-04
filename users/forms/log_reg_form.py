from django import forms
from django.contrib.auth import authenticate


class RegisterForm(forms.Form):
    username = forms.CharField(label="username")
    email = forms.CharField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="repeat_password", widget=forms.PasswordInput)

    # clean get automatically called during the authentication
    # use it to create custom requirements like password strength and check for correct password or valid email
    def clean(self):
        cleaned_deta = super().clean()
        username = cleaned_deta.get('username')
        password = cleaned_deta.get('password')
        repeat_password = cleaned_deta.get('repeat_password')
        email = cleaned_deta.get('email')

        if password != repeat_password:
            raise forms.ValidationError('Passwords do not match')

        validate_password(password)

        return cleaned_deta


from django import forms
from django.contrib.auth.password_validation import validate_password

# a bit of a useless form, might be usefull later
class LoginForm(forms.Form):
    email = forms.CharField(label="email")
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        email = cleaned_data.get('email')


        return cleaned_data
