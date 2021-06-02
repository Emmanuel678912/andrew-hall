from django.db import models

# Create your models here.
class TableA(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)

class TableB(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)   

class TableC(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)
    column4 = models.CharField(max_length=255, null=True, blank=True)    

class TableD(models.Model):
    first_octet = models.IntegerField(null=True, blank=True)
    second_octet = models.IntegerField(null=True, blank=True)
    third_octet = models.IntegerField(null=True, blank=True)
    fourth_octet = models.IntegerField(null=True, blank=True)
    subnet_mask = models.IntegerField(null=True, blank=True)

class TableE(models.Model):
    first_octet = models.IntegerField(null=True, blank=True)
    second_octet = models.IntegerField(null=True, blank=True)
    third_octet = models.IntegerField(null=True, blank=True)
    fourth_octet = models.IntegerField(null=True, blank=True)
    subnet_mask = models.IntegerField(null=True, blank=True)

class TableF(models.Model):
    first_octet = models.IntegerField(null=True, blank=True)
    second_octet = models.IntegerField(null=True, blank=True)
    third_octet = models.IntegerField(null=True, blank=True)
    fourth_octet = models.IntegerField(null=True, blank=True)
    subnet_mask = models.IntegerField(null=True, blank=True)
    variable = models.IntegerField(null=True, blank=True)

class TableG(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)
    
class TableH(models.Model):
    pass

