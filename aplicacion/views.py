from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola desde mi aplicación!")
# Create your views here.
