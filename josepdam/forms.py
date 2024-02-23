from django import forms
from .models import Search

class SearchForm (forms.ModelForm):
    address = forms.CharField(label='')
    class Meta :
        model = Search
        fields = ['address']

# this search is for map search different from the above location search
class SearchForm2(forms.Form):
    address = forms.CharField(label='')
    class Meta :
        model = Search
        fields = ['address']
