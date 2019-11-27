from roteamentornp.rotas.models import No
from roteamentornp.rotas.models import Estado 
from roteamentornp.rotas.models import Ligacao 
from collections import defaultdict
import datetime


class ProcuraMelhorRota:

    def __init__(self):
        pass

    def findNosEstado(self, estado):
        estatoObjeto = Estado.objects.filter(estado=estado)
        if estatoObjeto:
            return estatoObjeto
        return None


# Classe para montar as melhores rotas da RNP
class MontaRota:

    # Valores iniciais necessário para criação da rota é passado a data de pesquisa
    def __init__(self, dataPesquisa):
        self.vertices_id =  Estado.objects.all().values_list('id', flat=True) # lista dos ids dos estados
        self.list_vertice_id = list(self.vertices_id) # criação de uma lista de ids dos estaos no formato list
        self.vertices =  Estado.objects.all() # Recupera todos os estados
        self.grafo = defaultdict(list) # Cria um dicionário para os grafos
        self.vertexes = defaultdict(list) # Cria um dicionario para os vertices
        self.listaLatenciaMax = [] # Cria uma lista com as latências maximas das rotas escolhidas
        self.dataSeparada = dataPesquisa.split('-') # Separa as datas para uso dia, mes e ano separado
    

    # Adiciona a latência máxima de acordo com a pesquisa feita pela origem destino e pela data
    def add_pesos(self, src, dest):
        rotas = No.objects.filter(data_migration__year=self.dataSeparada[0],data_migration__month=self.dataSeparada[1],data_migration__day=self.dataSeparada[2], pop_dest_id=dest, pop_env_id=src)
        if len(rotas) == 0: # se não tiver mapeamento desta rota nesta data é retornado o valor 9999999 para que seja considerada uma rota inválida
            return 99999999
        return rotas[0].lat_max # retorna a latência máxima da rota que foi buscada na consulta
        
    # Cria um dicionaŕio com as melhores selecionadas e coloca em um dicionário para as rotas diretamente selecionadaas
    def criarDicionarioRotaSelecionada(self,melhoresRotas):
        rotasDictionary = defaultdict(list) # cria um dicionário das rotas
        ultimaRota = []
        for rota in range(len(melhoresRotas)): # faz um loop pelas melhores rotas
            listRota = melhoresRotas[rota] # coloca a cada rota em uma lista de rotas
            contador = 0
            ultimaRota = listRota
            for item in range(len(listRota) - 1): # faz um for entre os elementos das rotas
                itemArray = listRota[item] # verifica o item da rota
                contador+=1
                if not self.verifyHasItemInDictonary(rotasDictionary, itemArray, listRota[contador]): # verifica se o item e o item posterior já não estão no dicionário
                   rotasDictionary[itemArray].append(listRota[contador]) # aadiciona o item e o item posterior para o dicionaŕio

        rotasDictionary[ultimaRota[len(ultimaRota) -1]].append(0) # aciciona a ultima rota no dicionario
        return dict(rotasDictionary) # retrona o dicionario 



    def verifyHasItemInDictonary(self, dictonary, key, item):
        items = dictonary.get(key)
        if items != None:
            for i in range(len(items)):
                valor = items[i]
                if valor == item:
                    return True
        return False

    # cria um dicionaŕio com as ligações e os vertices de cada ligação direta e adiciona o peso para cada ligação
    def add_aresta(self, src, dest):
        cost = self.add_pesos(src,dest) # Adiciona o peso para a ligação direta
        self.grafo[src].append([dest, cost]) # cria um mapa com os nós de origem e destino
        self.vertexes[src].append(dest) # adiciona o vertice de destino so dicionário vertexes

    # Monta todas as todas as rotas que tem ligação direta
    def montarGrafo(self):
        self.todasRotas = Ligacao.objects.all() # Seleciona todas as ligações diretas
        for i in range(len(self.todasRotas)):
            rota = self.todasRotas[i]
            self.add_aresta(rota.origem_id, rota.destino_id) # adiciona as ligações diretas em um dicionario 
    
    # seleciona a melhor rota na data especificada
    def montarRota(self, paths=[]):
        menorPeso = 0 # define valor inicial do peso com 0
        melhorRota = [] # define valor da lista com a melhor rota vazia
        for i in range(len(paths) - 1):
            rota = paths[i] # seleciona uma rota dentro de todas as rotas possíveis
            pesoNo = 0
            for j in range(len(rota) - 1):
                origem = rota[j] # verifica o nó origem da rota
                destino = rota[j+1] # verifica o destino direto desta origem
                itemPeso = self.grafo.get(origem) # busca o peso desta origem
                pesoNo = pesoNo + self.getKey(destino, itemPeso) # Rerupera o valor buscando pela chave

            if menorPeso == 0: # Verifica se o peso é igual a 0
                menorPeso = pesoNo # Adiciona o valor do peso ao menor peso
                melhorRota = paths[i] # adiciona a melhor rota como o path
            elif pesoNo < menorPeso: # se o peso do nó for menor que o menor peso
                menorPeso = pesoNo # peso atual do nó substitui o peso do menor peso
                melhorRota = paths[i] # a melhor rota é substituida
        self.listaLatenciaMax.append(menorPeso) # é adicioanda a lista de latência o menor peso 
        return melhorRota # Retorna a melhor rota dentre todas as rotas possíveis
 

    # define as melhores rotas selecionadas de acordo com o total de rotas e o número de rotas a serem utilizadas
    def dfinirMelhoresRotas(self, numeroRotas, paths=[]):
        self.listaLatenciaMax.clear() # limpa a lista de latência máxima para não duplicar a melhor latência
        melhoresRotas = [] # cria a lista de melhores rotas 
        while numeroRotas > 0:
            rota = self.montarRota(paths) # seleciona a melhor rota
            index = paths.index(rota) # verifica o indice da melhor rota
            paths.pop(index) # remove a melhor rota da lista de paths
            melhoresRotas.append(rota) # adiciona a melhor rota na lista de melhores rotas
            numeroRotas -=1 # decrementa o numero de rotas
        return melhoresRotas # retorna as melhores rotas

    
    def getListaLatenciaMax(self):
        resultInt = []
        for valor in range(len(self.listaLatenciaMax)):
            resultInt.append(int(self.listaLatenciaMax[valor]))
        return resultInt

    # Retorna o valor passado uma chave e um dicionário
    def getKey(self, val, dictonary):
        for item in dictonary:
            if val == item[0]:
                return item[1]
        return None


    # Cria todos os caminhos possíveis da rota de origem para a rota de destino
    def findAllPaths(self, origem,destino, path=[]):
        path = path + [origem]
        
        # Se a origem for igual ao destino só existe uma rota
        if origem == destino:
            return [path]

        # Se não tiver o nó de origem então retorna vazio 
        if  len(self.vertexes.get(origem)) == 0:
            return []
        paths = []
        # verificar o possível caminho direto para o nó direto próximo
        for node in self.vertexes[origem]:
            # se o nó não estiver no path ele é dicionado como novo caminho 
            if node not in path:
                newpaths = self.findAllPaths(node, destino, path) # Feita uma chamada recursiva para montar o caminho ate o destino
                for newpath in newpaths:
                    paths.append(newpath) # adicionado o novo caminho a lista de paths
        return paths # retorna a lista de paths


# Classe de serviço para busca dos dados dos estados da tabela rotas_estado
class EstadosService:

    def __init__(self):
        pass

    # Consulta todos os dados da tabela rots_estado
    def findAllEstados(self):
        return Estado.objects.all() 