from django.shortcuts import render

def About(request):
    return render(request, 'About.html', {})