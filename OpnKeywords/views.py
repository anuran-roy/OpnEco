from django.shortcuts import render
from .scripts import keywords
# Create your views here.

def index(request):
    return render(request, 'OpnKeywords/index.html')

def analyze(request):
    data = request.POST.get('toAnalyze', 'default')
    op = keywords.execute(data)

    return render(request, 'OpnKeywords/results.html', {'fig': op})