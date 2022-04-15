from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.')

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']