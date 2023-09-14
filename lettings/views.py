"""
Defines the views of the lettings app.
Those views render the appropriate templates when called.
"""
from django.shortcuts import render
from lettings.models import Letting
from django.shortcuts import get_object_or_404


# Returns the lettings index page
def index(request):
    """
    View for the lettings app index page.
    This view retrieves all lettings listed in the db,
    and then renders the lettings/index.html template with them as context.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


# Returns the detailed view page of the letting passed as parameter
def letting(request, letting_id):
    """
    View for the detailed page of each letting.
    This view takes a letting id as a parameter.
    It retrieves it from the db,
    and then renders the lettings/letting.html template with it as context.
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
