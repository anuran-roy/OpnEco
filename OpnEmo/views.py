from django.shortcuts import render
from .scripts import emocheck
# Create your views here.

def index(request):
    return render(request, 'OpnEmo/index.html')

def analyze(request):
    data = request.POST.get('toAnalyze', 'default')
    op = emocheck.execute(data)

    return render(request, 'OpnEmo/results.html', {
        'val': op[0],
        # 'fig1': op[1],
        'fig2': op[1], #op[2],
        'fig3': op[2], #op[3],
        })