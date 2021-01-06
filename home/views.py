from django.shortcuts import render
from projects.models import Project

def home_view(request):
    return render(request, 'home.html', {})
