from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class RegisterForm(forms.Form):
    username = forms.CharField(label="username",required=True)
    email = forms.EmailField(label="email",required=True)
    password = forms.CharField(label="password", widget=forms.PasswordInput,required=True)
    repeat_password = forms.CharField(label="repeat_password", widget=forms.PasswordInput,required=True)

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


# a bit of a useless form, might be usefull later
class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email",required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput,required=True)

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')
        return cleaned_data
