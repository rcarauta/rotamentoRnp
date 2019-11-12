from django.db import models


class No(models.Model):
    data_migration  = models.DateTimeField()
    pop_env = models.CharField(max_length=100)
    pop_dest = models.CharField(max_length=100)
    perda_mdn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_min = models.DecimalField(max_digits=50, decimal_places=20)
    lat_med = models.DecimalField(max_digits=50, decimal_places=20)
    lat_max = models.DecimalField(max_digits=50, decimal_places=20)
    std_dvn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_ten_perc = models.DecimalField(max_digits=50, decimal_places=20)
    lat_mdn = models.DecimalField(max_digits=50, decimal_places=20)
    lat_nine_perc = models.DecimalField(max_digits=50, decimal_places=20)

    def __unicode__(self):
        return self.popEnv


