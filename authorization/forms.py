from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthenticationFormUser(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'username_login'}),
        label='Логин'
    )
    password = forms.CharField(
        max_length=30,
        widget=forms.PasswordInput(attrs={'class': 'password_login'}),
        label='Пароль'
    )
