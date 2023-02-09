from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html', context={'name' : 'Jojo'})

def sobre(request):
    return HttpResponse('Sobre')

def contato(request):
    return HttpResponse('Contato')