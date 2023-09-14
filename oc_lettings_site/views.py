from django.shortcuts import render


# Returns the home page of the app
def index(request):
    return render(request, 'index.html')


# Returns the error 404 page for the app
def handler404(request, exception):
    return render(request, '404.html', status=404)


# Returns the error 500 page for the app
def handler500(request):
    return render(request, '500.html', status=500)
