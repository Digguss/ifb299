from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group


class regpage(UserCreationForm):
    email = forms.EmailField(max_length = 100, required= True)
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), required= True)
    first_name = forms.CharField(max_length= 30, required= False)
    last_name = forms.CharField(max_length= 30, required= False)
    address = forms.CharField(max_length= 30, required = False)
    phonenumber = forms.CharField(max_length= 30, required = False)

    class Meta:
        model = User
        fields = ('username','password1', 'password2','email', 'groups','first_name', 'last_name', 'address', 'phonenumber')
        help_texts = {
            'username': "30 characters or less. Characters, digits and @/./+/-/_ only."
        }
