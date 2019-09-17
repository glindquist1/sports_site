from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import statsapi

from .forms import NameForm

def home(request):
	if request.method == 'POST':
		#creates a form instance, and populates it with the data from the request
		form = NameForm(request.POST)
		if form.is_valid():
			#when the data within the form is checked for validity, it is then stored in form.cleaned_data
			#return HttpResponseRedirect('/example/')
			context = {'post_output': statsapi.lookup_player(form.cleaned_data['search_name'])[0]['primaryNumber']}
			print(context)
			return render(request, 'sports/home.html', context)
			#render(request, 'sports/home.html', {'form': form})
		else:#if the form has not been submitted yet
			form = NameForm()
	#ie a GET request
	else:
		form = NameForm()

	return render(request, 'sports/home.html', {'form': form})