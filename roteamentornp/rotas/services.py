#from roteamentornp.rotas.models import No
#from roteamentornp.rotas.models import Estado 
#from roteamentornp.rotas.models import Ligacao 

class ProcuraMelhorRota:

    def __init__(self):
        pass

    def findBestRota(self, estado):
         objetoEstado = self.findNosEstado(estado)


    def findNosEstado(self, estado):
        pass
        #estatoObjeto = Estado.objects.filter(estado=estado)
        #if estatoObjeto:
         #   return estatoObjeto
        #return None


class MontaRota:

    def __init__(self):
        pass

    def montarRota(self,origem,destino):
        pass
        #listaRotas = Ligacao.objects.filter(origem=origem)
        #print(listaRotas)
        



class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()