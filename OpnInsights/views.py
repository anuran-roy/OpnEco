from django.shortcuts import render
from .scripts import trends
# Create your views here.

def index(request):
    return render(request, 'OpnInsights/index.html')

def analyze(request):
    data = request.POST.get('toAnalyze', 'default')
    op = trends.execute(data)

    return render(request, 'OpnInsights/results.html', {'fig': op[0]})