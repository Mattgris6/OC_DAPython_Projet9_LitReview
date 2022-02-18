from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    edit_signup = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', )


class LoginForm(forms.Form):
    edit_login = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')