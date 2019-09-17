from django import forms

class NameForm(forms.Form):
	search_name = forms.CharField(label='Player name', max_length=100)