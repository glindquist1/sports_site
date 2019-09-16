from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader
import statsapi

def index(request):
	# return HttpResponse("You're at the the sports index")
	x = statsapi.lookup_player('eloy jimenez')
	context = {'player_name': x}
	return render(request, 'sports/index.html', context)

# def home(request):
# 	#player = 
# 	return render(request, 'templates/sports/home.html', {
# 		'player_name': statsapi.lookup_player('eloy jimenez')
# 	})