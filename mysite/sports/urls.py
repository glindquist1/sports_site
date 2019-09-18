#I made this file (1)
from django.contrib import admin
from django.urls import path

from . import views
from mysite import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
	path('', views.home, name='home'),
	#path('plot', views.mplimage, name='mplimage')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)