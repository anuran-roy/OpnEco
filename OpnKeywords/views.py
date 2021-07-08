from django.shortcuts import render
from .scripts import keywords
# Create your views here.

def index(request):
    return render(request, 'OpnKeywords/index.html')

def analyze(request):
    data = request.POST.get('toAnalyze', 'default')
    knum = request.POST.get('numKeywords', 'default')

    try:
        knum = int(knum)
    except:
        knum = 10
    op = keywords.execute(knum, data)

    return render(request, 'OpnKeywords/results.html', {'fig': op})