from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User, Group

class searchform(forms.ModelForm):
    entry = forms.CharField(max_length = 100, required= True)

    class Meta:
        model = User
        fields = ()
