from django import forms



class userloginform(forms.form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
