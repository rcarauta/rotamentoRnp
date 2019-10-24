from roteamentornp.rotas.models import No
from roteamentornp.rotas.models import Estado 

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


class EstadosService:

    def __init__(self):
        pass


    def findAllEstados(self):
        return Estado.objects.all()