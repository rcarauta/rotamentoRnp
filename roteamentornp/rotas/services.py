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


class MontaRota:

    def __init__(self):
        self.vertices_id =  Estado.objects.all().values_list('id', flat=True)
        self.list_vertice_id = list(self.vertices_id)
        self.vertices =  Estado.objects.all()
        self.grafo = defaultdict(list)
        self.vertexes = defaultdict(list)
        self.listaLatenciaMax = []
    

    def add_pesos(self, src, dest):
        rotas = No.objects.filter(data_migration__year='2018',data_migration__month='09',data_migration__day='03', pop_dest_id=dest, pop_env_id=src)
        if len(rotas) == 0:
            return 99999999
        return rotas[0].lat_max
        

    def criarDicionarioRotaSelecionada(self,melhoresRotas):
        rotasDictionary = defaultdict(list)
        ultimaRota = []
        for rota in range(len(melhoresRotas)):
            listRota = melhoresRotas[rota]
            contador = 0
            ultimaRota = listRota
            for item in range(len(listRota) - 1):
                itemArray = listRota[item]
                contador+=1
                if not self.verifyHasItemInDictonary(rotasDictionary, itemArray, listRota[contador]):
                   rotasDictionary[itemArray].append(listRota[contador])

        rotasDictionary[ultimaRota[len(ultimaRota) -1]].append(0)
        return dict(rotasDictionary)



    def verifyHasItemInDictonary(self, dictonary, key, item):
        items = dictonary.get(key)
        if items != None:
            for i in range(len(items)):
                valor = items[i]
                if valor == item:
                    return True
        return False


    def add_aresta(self, src, dest):
        cost = self.add_pesos(src,dest)
        self.grafo[src].append([dest, cost])
        self.vertexes[src].append(dest)


    def montarGrafo(self):
        self.todasRotas = Ligacao.objects.all()
        for i in range(len(self.todasRotas)):
            rota = self.todasRotas[i]
            self.add_aresta(rota.origem_id, rota.destino_id)
    

    def montarRota(self, paths=[]):
        menorPeso = 0
        melhorRota = []
        for i in range(len(paths) - 1):
            rota = paths[i]
            pesoNo = 0
            for j in range(len(rota) - 1):
                origem = rota[j]
                destino = rota[j+1]
                itemPeso = self.grafo.get(origem)
                pesoNo = pesoNo + self.getKey(destino, itemPeso)

            if menorPeso == 0:
                menorPeso = pesoNo
                melhorRota = paths[i]
            elif pesoNo < menorPeso:
                menorPeso = pesoNo
                melhorRota = paths[i]
        self.listaLatenciaMax.append(menorPeso)
        return melhorRota 
 


    def dfinirMelhoresRotas(self, numeroRotas, paths=[]):
        self.listaLatenciaMax.clear()
        melhoresRotas = []
        while numeroRotas > 0:
            rota = self.montarRota(paths)
            index = paths.index(rota)
            paths.pop(index)
            melhoresRotas.append(rota)
            numeroRotas -=1
        return melhoresRotas


    def getListaLatenciaMax(self):
        resultInt = []
        for valor in range(len(self.listaLatenciaMax)):
            resultInt.append(int(self.listaLatenciaMax[valor]))
        return resultInt


    def getKey(self, val, dictonary):
        for item in dictonary:
            if val == item[0]:
                return item[1]
        return None


    def findAllPaths(self, origem,destino, path=[]):
        path = path + [origem]
        
        if origem == destino:
            return [path]

        if  len(self.vertexes.get(origem)) == 0:
            return []
        paths = []
        for node in self.vertexes[origem]:
            if node not in path:
                newpaths = self.findAllPaths(node, destino, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


    # https://www.python.org/doc/essays/graphs/


class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()