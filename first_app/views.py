from django.shortcuts import render

# Create your views here.
def index(request):
    dick = {'insert_me': "marechudi from first_app_views.py"}
    return render(request, 'first_app/index.html', context=dick)