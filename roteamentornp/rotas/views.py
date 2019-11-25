from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from roteamentornp.rotas.services import ProcuraMelhorRota
from roteamentornp.rotas.services import EstadosService
from roteamentornp.rotas.services import MontaRota
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    estado = EstadosService()
    todos = estado.findAllEstados()
    return render(request, 'index.html',{'options':todos, 'numeroRotas':0})


def montarRota(request):
     origem =  request.POST.get("origem","")
     destino = request.POST.get("destino", "")
     dataPesquisa = request.POST.get("dataPesquisa", "")
     rota = MontaRota(dataPesquisa)
     rota.montarGrafo()
     paths = rota.findAllPaths(int(origem), int(destino))
     melhorRota = rota.montarRota(paths)
     melhoresRotasLista  = rota.dfinirMelhoresRotas(4, paths)
     melhoresRotas = rota.criarDicionarioRotaSelecionada(melhoresRotasLista)
     estado = EstadosService()
     todos = estado.findAllEstados()
     lsitaLatenciaMax = rota.getListaLatenciaMax()
     print(melhoresRotasLista)
     print(melhoresRotas)
     print(len(paths))
     print(melhorRota)
     print(lsitaLatenciaMax)
     result = True
     return render(request, 'index.html', {'melhoresRotas': melhoresRotas, 'melhorRota': melhorRota, 'numeroRotas':len(paths), 'melhoresRotasLista': melhoresRotasLista, 'result':result, 'options':todos, 'listaLatenciaMax': lsitaLatenciaMax})
     

