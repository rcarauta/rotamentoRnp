from django.db import models


class Estado(models.Model):
    estado = models.CharField(max_length=100)

    def __unicode__(self):
        return self.estado

class No(models.Model):
    data  = models.DateTimeField()
    popEnv = models.CharField(max_length=100)
    popDest = models.ForeignKey('No', null=True, on_delete=models.SET_NULL)
    perdaMdn = models.IntegerField()
    latMin = models.IntegerField()
    latMed = models.IntegerField()
    latMax = models.IntegerField()
    stdDvn = models.IntegerField()
    latTenPerc = models.IntegerField()
    latMdn = models.IntegerField()
    latNinePerc = models.IntegerField()
    estado = models.ForeignKey('Estado', null=True, on_delete=models.SET_NULL)



    def __unicode__(self):
        return self.popEnv

