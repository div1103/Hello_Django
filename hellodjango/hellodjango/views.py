from django.http import HttpResponse
from django.shortcuts import render

def adout(request):
    return render(request, 'about.html', {'gretting':'hello'})

def home(request):
    return HttpResponse('This is my home')