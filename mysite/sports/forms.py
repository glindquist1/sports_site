from django import forms

class NameForm(forms.Form):
	search_text = forms.CharField(label='search_text', max_length=100)