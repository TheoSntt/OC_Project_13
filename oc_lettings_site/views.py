"""
Defines the views of the website that do not belong to the profiles or the lettings app.
As of now, it only defines the home page view, which renders the index.html template.
"""
from django.shortcuts import render
import logging


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Returns the home page of the app
def index(request):
    """
    View for the home page of the website.
    Straightforward : returns the index.html template when called.
    """
    logger.info("Home page view rendered")
    return render(request, 'index.html')
