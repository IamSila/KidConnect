from django.shortcuts import render
from . models import Analytic
from . models import Team

# Create your views here.
def index(request):
    context = {}
    Analytics = Analytic.objects.all()
    context['analytics'] = Analytics

    """getting all team members"""
    Teams = Team.objects.all()
    context['Teams'] = Teams
    return render(request, 'index.html', context)