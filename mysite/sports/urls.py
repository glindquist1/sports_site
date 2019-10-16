#I made this file (1)
from django.contrib import admin
from django.urls import path

from . import views
from mysite import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

#from .views import HomeView, ChartData
from .views import HomeView, get_data, ChartData

urlpatterns = [
	path('', HomeView.as_view(), name='home'),
	#path('plot', views.mplimage, name='mplimage')
	path('api/data/', get_data, name='api-data'),
	path('api/chart/data/', ChartData.as_view()),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)