from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from roteamentornp.rotas.services import ProcuraMelhorRota
from roteamentornp.rotas.services import EstadosService
from roteamentornp.rotas.services import MontaRota

def index(request):
    estado = EstadosService()
    todos = estado.findAllEstados()
    return render(request, 'index.html',{'options':todos})


def montarRota(request):
     origem =  request.POST.get("origem","")
     destino = request.POST.get("destino", "")
     rota = MontaRota()
     rotaMontada = rota.montarRota(origem,destino)
     

