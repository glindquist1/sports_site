#I made this file (1)
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name='home'),
	#path('', views.index, name='index')
]