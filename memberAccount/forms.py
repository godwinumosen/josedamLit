
from .models import memberRegister
from django import forms

class MyForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length = 50)
