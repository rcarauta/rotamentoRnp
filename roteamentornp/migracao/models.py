from django.db import models


class No(models.Model):
    data  = models.DateTimeField()
    popEnv = models.CharField(max_length=100)
    popDest = models.CharField(max_length=100)
    perdaMdn = models.IntegerField()
    latMin = models.IntegerField()
    latMed = models.IntegerField()
    latMax = models.IntegerField()
    stdDvn = models.IntegerField()
    latTenPerc = models.IntegerField()
    latMdn = models.IntegerField()
    latNinePerc = models.IntegerField()

    def __unicode__(self):
        return self.popEnv


