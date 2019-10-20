from django.db import models

class No(models.Model):
    origem = models.CharField(max_length=100)
    destino = models.ForeignKey("No", on_delete=models.CASCADE)
    peso = models.IntegerField()

    def __unicode__(self):
        return self.origem

