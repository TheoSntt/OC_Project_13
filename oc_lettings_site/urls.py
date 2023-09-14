"""
Defines the url routes for the website.
It indicates, for each URL, which view should be called.
It also imports the url routes of both lettings and profiles apps.
"""
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
