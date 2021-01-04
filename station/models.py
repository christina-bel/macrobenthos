from django.db import models

# Create your models here.

class Station(models.Model):
    descr = models.CharField('Описание', max_length=2000)
    ddate = models.DateTimeField('Дата сбора')
    code  = models.CharField('Код', max_length=255, blank=True)
    num   = models.IntegerField('Номер', blank=True)
    def __str__(self):
        return f"{self.num} {self.descr}"
