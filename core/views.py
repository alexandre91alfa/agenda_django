from django.shortcuts import render, HttpResponse
import json
from core.models import Evento

# Create your views here.


def consulta_Titulo_Evento(response, id):
    consulta = Evento.objects.get(id=id)
    jsonx = f'''
        <h1>{consulta.titulo}</h1>\n
        <ul>
        <li>nome Usuario : {consulta.usuario}\n</li>
        <li>descricao : {consulta.descricao}\n</li>
        <li>Data : {consulta.data_evento}</li>
        </ul>
    '''
    return HttpResponse(jsonx)


# def index(request):
#     return redirect("/agenda/")


def home(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)
