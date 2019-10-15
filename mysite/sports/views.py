# from django.shortcuts import render
# from django.http import HttpResponse
# #from django.template import loader
# import statsapi

# from pylab import figure, axes, pie, title
# import matplotlib
# import matplotlib.pyplot as plt
# from matplotlib.backends.backend_agg import FigureCanvasAgg
# import io
# from django.core.files import File

# from .forms import NameForm
# from .models import GraphResult

# from mysite import settings

# import numpy as np


from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

#option 1
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'sports/home.html', {"customers": 10})
#option 3
def get_data(request, *args, **kwargs):
	#this is where i call the mlb api
	data = {
		"sales": 100,
		"customers": 10,
	}
	return JsonResponse(data)


#option 2
#USE THIS ONE
class ChartData(APIView):
	#allow you to get data based on some authentication or permission
	authentication_classes = []
	permission_classes = []

	def get(self, request, format=None):
		labels = ['Player1', 'p2', 'p3', 'p4']
		default_items = [7, 8, 1, 2]
		data = {
			"labels": labels,
			"default": default_items,

		}
		return Response(data)

# class ListUsers(APIView):
#     """
#     View to list all users in the system.

#     * Requires token authentication.
#     * Only admin users are able to access this view.
#     """
#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAdminUser]

#     def get(self, request, format=None):
#         """
#         Return a list of all users.
#         """
#         usernames = [user.username for user in User.objects.all()]
#         return Response(usernames)



###############
# def home(request):
# 	if request.method == 'GET':

# 		print(settings.BASE_DIR)
# 		#creates a form instance, and populates it with the data from the request
# 		form = NameForm(request.GET)
# 		if form.is_valid():
# 			#when the data within the form is checked for validity, it is then stored in form.cleaned_data
# 			#return HttpResponseRedirect('/example/')

# 			#print(context)
# 			img = createimage()
# 			context = {'number_output': statsapi.lookup_player(form.cleaned_data['search_name'])[0]['primaryNumber'],
# 						'image': img}
# 			return render(request, 'sports/home.html', context)
# 			#render(request, 'sports/home.html', {'form': form})
# 		else:#if the form has not been submitted yet
# 			form = NameForm()
# 	#ie a GET request
# 	else:
# 		form = NameForm()

# 	return render(request, 'sports/home.html', {'form': form})

# def createimage():
# 	# f = matplotlib.figure.Figure()

# 	# # Code that sets up figure goes here; in the question, that's ...
# 	# FigureCanvasAgg(f)
# 	t = np.arange(0.0, 2.0, 0.01)
# 	s = 1 + np.sin(2 * np.pi * t)

# 	fig, ax = plt.subplots()
# 	ax.plot(t, s)

# 	ax.set(xlabel='time (s)', ylabel='voltage (mV)',
# 		   title='About as simple as it gets, folks')
# 	ax.grid()

# 	#fig.savefig("test.png")


# 	buf = io.BytesIO()
# 	fig.savefig('media/foo.png')
# 	#fig.savefig(buf, format='png')
# 	#plt.savefig(buf, format='png')
# 	#plt.close(f)
# 	#response = HttpResponse(buf.getvalue(), content_type='image/png')
	
# 	g = GraphResult()
# 	#File('graph.png', buf)
# 	g.photo = 'foo.png'
# 	#g.save('graph.png', File(buf), save=False) 
# 	g.save()
# 	return g
# 	#return response
# 	#return buf.getvalue()