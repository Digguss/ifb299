from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class editform(UserCreationForm):
    email = forms.EmailField(max_length = 100, required= True)
    first_name = forms.CharField(max_length= 30, required= False)
    last_name = forms.CharField(max_length= 30, required= False)
    address = forms.CharField(max_length= 30, required = False)

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'address')