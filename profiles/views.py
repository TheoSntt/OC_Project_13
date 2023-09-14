from django.shortcuts import render
from profiles.models import Profile
from django.shortcuts import get_object_or_404


# Returns the profiles index page
def index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Returns the detailed view page of the profile passed as parameter
def profile(request, username):
    # profile = Profile.objects.get(user__username=username)
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
