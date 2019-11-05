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
        self.numero_rotas = 0
    

    def add_pesos(self, src, dest):
        rotas = No.objects.filter(data_migration__date=datetime.date(2018, 9, 3), pop_dest_id=dest, pop_env_id=src)
        if len(rotas) == 0:
            return 99999999
        return rotas[0].lat_max
        

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

        return melhorRota
 


    def dfinirMelhoresRotas(self, numeroRotas, paths=[]):
        melhoresRotas = []
        while numeroRotas > 0:
            rota = self.montarRota(paths)
            index = paths.index(rota)
            paths.pop(index)
            melhoresRotas.append(rota)
            numeroRotas -=1
        return melhoresRotas



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
                    self.numero_rotas += 1
                    paths.append(newpath)
        return paths


    def getNumeroRotas(self):
        return self.numero_rotas


    # https://www.python.org/doc/essays/graphs/


class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()