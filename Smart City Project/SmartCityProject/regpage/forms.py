from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class regpage(UserCreationForm):
    email = forms.EmailField(max_length = 100, required= True)
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), label="Account Type", required= True)

    class Meta:
        model = User
        fields = ('username','password1', 'password2','email', 'groups')
        help_texts = {
            'username': "30 characters or less. Characters, digits and @/./+/-/_ only."
        }
