from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.template.response import TemplateResponse
from roteamentornp.rotas.services import ProcuraMelhorRota
from roteamentornp.rotas.services import EstadosService
from roteamentornp.rotas.services import MontaRota
import json
from django.core.serializers.json import DjangoJSONEncoder

# Método chamado ao iniciar a tela
def index(request):
    estado = EstadosService() # Instancia a classe EstadoService 
    todos = estado.findAllEstados() # seleciona todos os estados
    # retorna todos os estados e o número de rotas como 0 para a tela inicial
    return render(request, 'index.html',{'options':todos, 'numeroRotas':0})

# Método chamado ao clicar no botão pesquisar da tela
def montarRota(request):
     origem =  request.POST.get("origem","") # Pega o valor enviado via post do nó de origem
     destino = request.POST.get("destino", "") # Pega o valor enviado via post do nó de destino
     dataPesquisa = request.POST.get("dataPesquisa", "") # pega o valor enviado via post do nó da data da pesquisa
     rota = MontaRota(dataPesquisa) # instancia a classe MontaRota com a data de pesquisa
     rota.montarGrafo() # Monta todas as rotas que tem ligação direta
     paths = rota.findAllPaths(int(origem), int(destino)) # Monta todas as possíveis rotas entre a origem e o destino e adiciona me uma matriz
     melhorRota = rota.montarRota(paths) # Define qual a melhor rota 
     melhoresRotasLista  = rota.dfinirMelhoresRotas(4, paths) # Define o array com as melhores  rotas 
     melhoresRotas = rota.criarDicionarioRotaSelecionada(melhoresRotasLista) # cria um dicionário com as melhores rotas e quais são as ligações diretas entre elas
     estado = EstadosService() # Instâmncia a classe EstadoService
     todos = estado.findAllEstados() # Seleiona todos os estados
     lsitaLatenciaMax = rota.getListaLatenciaMax() # Verifica a lista com a latência máxima das rotas selecionadas
     listaLatenciaMin = rota.getListaLatenciaMin() # Verifica a latencia mínima das rotas selecionadas
     print(listaLatenciaMin)
     result = True # Faz aparecer o svg com as rotas na tela
     # retorna os dados para a tela 
     return render(request, 'index.html', {'melhoresRotas': melhoresRotas, 'melhorRota': melhorRota, 'numeroRotas':len(paths), 'melhoresRotasLista': melhoresRotasLista, 'result':result, 'options':todos, 'listaLatenciaMax': lsitaLatenciaMax, 'listaLatenciaMin':listaLatenciaMin})
     

