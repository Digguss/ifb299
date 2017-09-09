from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class regpage(UserCreationForm):
    email = forms.EmailField(max_length = 100, help_text ='Required Field')

    class meta:
        model = User
        fields = ('username','password','email',)
