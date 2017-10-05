from django import forms
from django.contrib.auth.forms import SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User, Group

class editform(forms.ModelForm):
    email = forms.EmailField(max_length = 100, required= False)
    first_name = forms.CharField(max_length= 30, required= False)
    last_name = forms.CharField(max_length= 30, required= False)
    address = forms.CharField(max_length= 30, required = False)

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'address')


class changepasswordform(PasswordChangeForm):

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')
