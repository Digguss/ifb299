from django import forms
from .models import hotel

class enterhotelinfo(forms.ModelForm):
    class Meta:
        model = hotel
        fields = ('name','descrption','phonenumber','address','image')
