from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

@login_required(login_url='/login/')
def home(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido!!!")
    return redirect('/login')
