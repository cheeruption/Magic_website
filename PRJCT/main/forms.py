from django import forms



class SearchForm(forms.Form):
    cardname = forms.CharField(
        label='Cardname', max_length=150,
        )