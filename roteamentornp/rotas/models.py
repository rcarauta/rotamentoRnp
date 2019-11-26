from django.db import models


# Classe para referenciar o Modelo de dados da tabela rotas_estado
class Estado(models.Model):
    estado = models.CharField(max_length=100)

    def __unicode__(self):
        return self.estado 

# Classe para referenciar o Modelo de dados da tabela rota_no
class No(models.Model):
    data_migration  = models.DateTimeField()
    pop_env = models.ForeignKey(Estado, null=True,related_name="pop_env_estado", on_delete=models.SET_NULL)
    pop_dest = models.ForeignKey(Estado, null=True,related_name="pop_dest_estado", on_delete=models.SET_NULL)
    perda_mdn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_min = models.DecimalField(max_digits=50, decimal_places=20)
    lat_med = models.DecimalField(max_digits=50, decimal_places=20)
    lat_max = models.DecimalField(max_digits=50, decimal_places=20)
    std_dvn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_ten_perc = models.DecimalField(max_digits=50, decimal_places=20)
    lat_mdn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_nine_perc = models.DecimalField(max_digits=50, decimal_places=20)


    def __unicode__(self):
        return self.data_migration


# Classe para referenciar o Modelo de dados da tabela rotas_ligacao
class Ligacao(models.Model):
    origem = models.ForeignKey(Estado, null=True,related_name="origem_estado", on_delete=models.SET_NULL)
    destino = models.ForeignKey(Estado, null=True,related_name="destino_estado", on_delete=models.SET_NULL)
    link_ativo = models.BooleanField(default=True)

