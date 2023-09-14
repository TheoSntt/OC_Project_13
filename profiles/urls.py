"""
Defines the url routes of the profiles app.
It indicates, for each URL, which view should be called.
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='profiles_index'),
    path('<str:username>/', views.profile, name='profile'),
]
