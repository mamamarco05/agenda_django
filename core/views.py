from django.shortcuts import render, HttpResponse
from core.models import Evento

# Create your views here.

def evento(requests, titulo_evento):
    objeto = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse('<p>{}</p><p>{}</p>'.format(objeto.titulo,objeto.data_evento))

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)