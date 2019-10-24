from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from roteamentornp.rotas.services import ProcuraMelhorRota
from roteamentornp.rotas.services import EstadosService

def index(request):
    t = loader.get_template('index.html')
    estado = EstadosService()
    todos = estado.findAllEstados()
    return HttpResponse(t.render({'options':todos}))



