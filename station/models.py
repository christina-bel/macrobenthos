from django.db import models

# Create your models here.

class Station(models.Model):
    descr = models.CharField('Описание', max_length=2000)
    ddate = models.DateTimeField('Дата сбора')
    code  = models.CharField('Код', max_length=255, blank=True, null=True)
    num   = models.IntegerField('Номер', blank=True, null=True)
    def __str__(self):
        return f"{self.num} {self.descr}"
        
    class Meta:
        db_table = "station"

class Ship(models.Model):
    name = models.CharField('Наименование', max_length=255)
    eng_name = models.CharField('Английское наименование', max_length=255, blank=True, null=True)
    code  = models.CharField('Код', max_length=100, blank=True, null=True)
    descr = models.CharField('Описание', max_length=2000, blank=True, null=True)
    descr_st = models.CharField('Описание станций', max_length=100, blank=True, null=True)
    descr_worm = models.CharField('Описание червей', max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.name} {self.code} {self.descr}"
        
    class Meta:
        db_table = "ship"
