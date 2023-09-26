"""
Defines the views of the profiles app.
Those views render the appropriate templates when called.
"""
from django.shortcuts import render
from profiles.models import Profile
from django.http import Http404
from django.shortcuts import get_object_or_404
import logging


# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


# Returns the profiles index page
def index(request):
    """
    View for the profiles app index page.
    This view retrieves all profiles listed in the db,
    and then renders the profiles/index.html template with them as context.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    logger.info("List view rendered for profiles :", extra=context)
    return render(request, 'profiles/index.html', context)


# Returns the detailed view page of the profile passed as parameter
def profile(request, username):
    """
    View for the detailed page of each profile.
    This view takes a profile username as a parameter.
    It retrieves it from the db,
    and then renders the profiles/profile.html template with it as context.
    """
    try:
        # profile = Profile.objects.get(user__username=username)
        profile = get_object_or_404(Profile, user__username=username)
        context = {'profile': profile}
        logger.info("Detailed view rendered for profile :", extra=context)
        return render(request, 'profiles/profile.html', context)
    except Http404:
        logger.error("Error 404 happened on profiles", exc_info=True)
        raise
