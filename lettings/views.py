"""
Defines the views of the lettings app.
Those views render the appropriate templates when called.
"""
from django.shortcuts import render
from lettings.models import Letting
from django.http import Http404
from django.shortcuts import get_object_or_404
import logging


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Returns the lettings index page
def index(request):
    """
    View for the lettings app index page.
    This view retrieves all lettings listed in the db,
    and then renders the lettings/index.html template with them as context.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    logger.info("List view rendered for lettings :", extra=context)
    return render(request, 'lettings/index.html', context)


# Returns the detailed view page of the letting passed as parameter
def letting(request, letting_id):
    """
    View for the detailed page of each letting.
    This view takes a letting id as a parameter.
    It retrieves it from the db,
    and then renders the lettings/letting.html template with it as context.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        logger.info("Detailed view rendered for letting :", extra=context)
        return render(request, 'lettings/letting.html', context)
    except Http404:
        logger.error("Error 404 happened on lettings", exc_info=True)
        raise
