from django.db import models


class Estacao(models.Model):
    estacao = models.CharField(max_length=100)

    def __unicode__(self):
        return self.estacao


class Distancia(models.Model):
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    nascimento = models.DateTimeField()
    pais = models.CharField(max_length=2)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    datacadastramento = models.DateTimeField()
    projeto = models.CharField(max_length=100)
    datacorrida = models.DateTimeField()
    diasemana = models.CharField(max_length=100)
    horaretirada = models.TimeField()
    estacaoretirada = models.ForeignKey(Estacao, null=True,related_name="estacaoretirada_fk", on_delete=models.SET_NULL)
    areaestacaoretirada = models.CharField(max_length=100)
    enderecoestacaoretirada = models.CharField(max_length=200)
    meioretirada = models.CharField(max_length=100)
    horadevolucao = models.TimeField()
    estacaodevolucao = models.ForeignKey(Estacao, null=True,related_name="estacaodevolucao_fk", on_delete=models.SET_NULL)
    areaestacaodevolucao = models.CharField(max_length=100)
    enderecoestacaodevolucao = models.CharField(max_length=200)
    duracaocorrida = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome


# class Ligacao(models.Model):
#     origem = models.ForeignKey(Estado, null=True,related_name="origem_estado", on_delete=models.SET_NULL)
#     destino = models.ForeignKey(Estado, null=True,related_name="destino_estado", on_delete=models.SET_NULL)
#     link_ativo = models.BooleanField(default=True)

