from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import statsapi

from pylab import figure, axes, pie, title
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
import io
from django.core.files import File

from .forms import NameForm
from .models import GraphResult

from mysite import settings

import numpy as np

def home(request):
	if request.method == 'GET':

		print(settings.BASE_DIR)
		#creates a form instance, and populates it with the data from the request
		form = NameForm(request.GET)
		if form.is_valid():
			#when the data within the form is checked for validity, it is then stored in form.cleaned_data
			#return HttpResponseRedirect('/example/')

			#print(context)
			img = createimage()
			context = {'number_output': statsapi.lookup_player(form.cleaned_data['search_name'])[0]['primaryNumber'],
						'image': img}
			return render(request, 'sports/home.html', context)
			#render(request, 'sports/home.html', {'form': form})
		else:#if the form has not been submitted yet
			form = NameForm()
	#ie a GET request
	else:
		form = NameForm()

	return render(request, 'sports/home.html', {'form': form})

def createimage():
	# f = matplotlib.figure.Figure()

	# # Code that sets up figure goes here; in the question, that's ...
	# FigureCanvasAgg(f)
	t = np.arange(0.0, 2.0, 0.01)
	s = 1 + np.sin(2 * np.pi * t)

	fig, ax = plt.subplots()
	ax.plot(t, s)

	ax.set(xlabel='time (s)', ylabel='voltage (mV)',
		   title='About as simple as it gets, folks')
	ax.grid()

	#fig.savefig("test.png")


	buf = io.BytesIO()
	fig.savefig('media/foo.png')
	#fig.savefig(buf, format='png')
	#plt.savefig(buf, format='png')
	#plt.close(f)
	#response = HttpResponse(buf.getvalue(), content_type='image/png')
	
	g = GraphResult()
	#File('graph.png', buf)
	g.photo = 'foo.png'
	#g.save('graph.png', File(buf), save=False) 
	g.save()
	return g
	#return response
	#return buf.getvalue()