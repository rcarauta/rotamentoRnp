from django.db import models


class No(models.Model):
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
    estacaoretirada = models.CharField(max_length=100)
    areaestacaoretirada = models.CharField(max_length=100)
    enderecoestacaoretirada = models.CharField(max_length=200)
    meioretirada = models.CharField(max_length=100)
    horadevolucao = models.TimeField()
    estacaodevolucao = models.CharField(max_length=100)
    areaestacaodevolucao = models.CharField(max_length=100)
    enderecoestacaodevolucao = models.CharField(max_length=200)
    duracaocorrida = models.CharField(max_length=100)


    def __unicode__(self):
        return self.nome


