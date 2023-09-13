from django.shortcuts import render


# Returns the home page of the app
def index(request):
    return render(request, 'index.html')
