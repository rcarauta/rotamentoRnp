from roteamentornp.rotas.models import No
from roteamentornp.rotas.models import Estado 
from roteamentornp.rotas.models import Ligacao 
from collections import defaultdict
import heapq
import datetime


class MinHeap:

	def __init__(self):
		self._queue = []
		self._index = 0

	def insert(self, item, priority):
		heapq.heappush(self._queue, (-priority, self._index, item))
		self._index += 1

	def remove(self):
		return heapq.heappop(self._queue)[-1]

	def get_length(self):
		return len(self._queue)


class ProcuraMelhorRota:

    def __init__(self):
        pass

    def findBestRota(self, estado):
         objetoEstado = self.findNosEstado(estado)


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
       # self.grafo = [[0] * len(self.list_vertice_id) for i in range(len(self.list_vertice_id))]
        self.grafo = defaultdict(list)
        self.vertexes = {}
    

    def add_pesos(self, src, dest):
        rotas = No.objects.filter(data_migration__date=datetime.date(2018, 9, 3), pop_dest_id=dest, pop_env_id=src)
        if len(rotas) == 0:
            return 99999999
        return rotas[0].lat_max
        

    def add_aresta(self, src, dest):
        cost = self.add_pesos(src,dest)
        self.grafo[src].append([dest, cost])
        self.vertexes[src] = src
        self.vertexes[dest] = dest


    def montarGrafo(self):
        self.todasRotas = Ligacao.objects.all()
        for i in range(len(self.todasRotas)):
            rota = self.todasRotas[i]
            self.add_aresta(rota.origem_id, rota.destino_id)
        print(self.grafo)
    

    def montarRota(self,src,dest):
        number_vertexes = len(self.vertexes)
        p = [None for i in range(number_vertexes)]
        p[src] = 0
        
        min_heap = MinHeap()
        min_heap.insert(src, 0)

        while min_heap.get_length() > 0:
            u = min_heap.remove()

            for edge in self.grafo[u]:

                v, cost = edge
                if  p[v] is None or p[v] > p[u] + cost:
                    p[v] = p[u] + cost
                    min_heap.insert(v,p[v])
        return p[dest]



class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()