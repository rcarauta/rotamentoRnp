from roteamentornp.rotas.models import No
from roteamentornp.rotas.models import Estado 
from roteamentornp.rotas.models import Ligacao 

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
        self.grafo = [[0] * len(self.list_vertice_id) for i in range(len(self.list_vertice_id))]


    def add_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1


    def montarGrafo(self):
        self.todasRotas = Ligacao.objects.all()
        for i in range(len(self.todasRotas)):
            rota = self.todasRotas[i]
            self.add_aresta(rota.origem_id, rota.destino_id)

        

    def montarRota(self,origem,destino):
        listaRotas = Ligacao.objects.filter(origem=origem)
        visitados = [False] * len(self.vertices)
        visitados[origem - 1] = True
        fila = [origem - 1]

        while len(fila) > 0:
            origem = fila[0]

            for u in range(len(self.vertices_id)):
                if self.grafo[origem][u] == 1:
                    if visitados[u] == False:
                        visitados[u] = True
                        estado = self.vertices[u]
                        fila.append(u)
                        print('%s visitado' % estado.estado)
            fila.pop(0)


class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()