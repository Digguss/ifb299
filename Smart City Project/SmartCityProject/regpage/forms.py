from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class regpage(UserCreationForm):
    email = forms.EmailField(max_length = 100, help_text ='Required Field', required= True)
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), required= True)

    class Meta:
        model = User
        fields = ('username','password1', 'password2','email', 'groups')
