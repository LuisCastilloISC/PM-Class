from django.shortcuts import render
from personas.models import Persona
# Create your views here.
def index(request):
    return render(request,'bienvenido.html')


def indexPersonas(request):
    noPersonas = Persona.objects.count()
    personas = Persona.objects.order_by('id')

    return render(request,'indexPersonas.html',{'noPersonas':noPersonas,'personas':personas})
