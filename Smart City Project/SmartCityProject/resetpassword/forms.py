from django import forms
from django.contrib.auth.models import User

class resetpasswordform(forms.ModelForm):
    username = forms.CharField(max_length = 150, required = True)
    email = forms.EmailField(max_length = 100, required= True)

    class Meta:
        model = User
        fields = ('username','email')
