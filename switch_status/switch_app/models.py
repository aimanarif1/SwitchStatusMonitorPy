from django.db import models

class Terminals(models.Model):
    switch_label = models.CharField(max_length=50)
    t1 = models.IntegerField()
    t2 = models.IntegerField()
    t3 = models.IntegerField()
    t4 = models.IntegerField()
    t5 = models.IntegerField()
    timestamp = models.DateTimeField()
