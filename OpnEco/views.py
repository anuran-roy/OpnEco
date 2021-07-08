from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'OpnEco/index.html')

def settings(request):
    return render(request, 'OpnEco/settings.html')

def about(request):
    return render(request, 'OpnEco/about.html')