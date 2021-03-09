from django.db import models

# Create your models here. 

class Ship(models.Model):
    name = models.CharField('Наименование', max_length=255)
    eng_name = models.CharField('Английское наименование', max_length=255, blank=True, null=True)
    code  = models.CharField('Код', max_length=100, blank=True, null=True)
    descr = models.CharField('Описание', max_length=2000, blank=True, null=True)
    descr_st = models.CharField('Описание станций', max_length=100, blank=True, null=True)
    descr_worm = models.CharField('Описание червей', max_length=100, blank=True, null=True)
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = "ship"
        ordering = ['name']
        
        
class Family(models.Model):
    family = models.CharField('Семейство', max_length=255, unique=True)
    def __str__(self):
        return f"{self.family}"
        
    class Meta:
        db_table = "family"
        ordering = ['family']
        

class Genus(models.Model):
    name = models.CharField('Родовое название', max_length=255, unique=True)
    family_name = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Семейство', related_name='genus_name')
    def __str__(self):
        return f"{self.name}"
        
    class Meta:
        db_table = "genus"
        ordering = ['name']
        
class Species(models.Model):
    name = models.CharField('Название', max_length=255)
    genus_name = models.ForeignKey(Genus, on_delete=models.CASCADE, verbose_name='Родовое название')
    species_name = models.CharField('Видовое название', max_length=255, blank=True, null=True)
    author = models.CharField('Автор', max_length=50, blank=True, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, verbose_name='Семейство')
    remark = models.CharField('Примечание', max_length=150, blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.family})"
        
    class Meta:
        db_table = "species"
        ordering = ['name']
        

class Samples(models.Model):
    sample_num =  models.PositiveIntegerField('Номер пробы', default=1)
    subsample_num =  models.PositiveIntegerField('Номер подпробы', default=1)
    species = models.ForeignKey(Species, on_delete = models.CASCADE, verbose_name='Вид')
    weight = models.FloatField('Масса', blank=True, null=True, default=0.0)
    def __str__(self):
        return f"№{self.sample_num} - {self.species}"
    
    class Meta:
        db_table = "samples"
        ordering = ['sample_num', 'subsample_num']

class Station(models.Model):
    num = models.IntegerField('Номер станции', default=0)
    ship_code = models.ForeignKey(Ship, verbose_name='Код судна', on_delete=models.CASCADE)
    cruise = models.CharField('Код рейса', max_length=255, default='0')
    latitude = models.DecimalField('Широта', max_digits=9, decimal_places=6, default=0.0)
    longitude = models.DecimalField('Долгота', max_digits=9, decimal_places=6, default=0.0)
    ddate = models.DateTimeField('Дата сбора', blank=True, null=True)
    sample = models.ManyToManyField(Samples, related_name='station', verbose_name='Проба')
    rem = models.CharField('Примечание', max_length=2000, blank=True, null=True)
    def __str__(self):
        return f"{self.num} {self.ship_code}"
    
    class Meta:
        db_table = "station"
        ordering = ['num']
