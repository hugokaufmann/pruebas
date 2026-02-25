from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Hola desde mi aplicación!")


def hola(request):
    return HttpResponse("Ahora tengo otra url sin parámetros")
# Create your views here.
