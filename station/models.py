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
        
class Family(models.Model):
    family = models.CharField('Семейство', max_length=255, unique=True)
    def __str__(self):
        return f"{self.family}"
        
    class Meta:
        db_table = "family"
        

class Genus(models.Model):
    name = models.CharField('Родовое название', max_length=255, unique=True)
    family_name = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Семейство', related_name='genus_name')
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = "genus"
        
class Species(models.Model):
    name = models.CharField('Название', max_length=255)
    genus_name = models.ForeignKey(Genus, on_delete=models.CASCADE, verbose_name='Родовое название')
    species_name = models.CharField('Видовое название', max_length=255, blank=True, null=True)
    author = models.CharField('Автор', max_length=50, blank=True, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Семейство')
    remark = models.CharField('Примечание', max_length=150, blank=True, null=True)
    def __str__(self):
        return f"{self.name} {self.family} {self.remark}"
        
    class Meta:
        db_table = "species"
        ordering = ['name']

