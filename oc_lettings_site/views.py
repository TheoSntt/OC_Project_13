"""
Defines the views of the website that do not belong to the profiles or the lettings app.
As of now, it only defines the home page view, which renders the index.html template.
"""
from django.shortcuts import render


# Returns the home page of the app
def index(request):
    """
    View for the home page of the website.
    Straightforward : returns the index.html template when called.
    """
    return render(request, 'index.html')
