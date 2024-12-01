from django.shortcuts import render
from . models import Analytic

# Create your views here.
def index(request):
    context = {}
    Analytics = Analytic.objects.all()
    context['analytics'] = Analytics
    
    return render(request, 'index.html', context)