from django.db import models

# Create your models here.
class TableA(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)

class TableB(models.Model):
    column2 = models.CharField(max_length=255, null=True, blank=True)   

class TableC(models.Model):
    CHOICES = [
        ("Value 1", ''),
        ("Value 2", "")
    ]

    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)
    column4 = models.CharField(max_length=255, null=True, blank=True, choices=CHOICES)    

class TableD(models.Model):
    first_octet = models.IntegerField(null=True, blank=True)
    second_octet = models.IntegerField(null=True, blank=True)
    third_octet = models.IntegerField(null=True, blank=True)
    fourth_octet = models.IntegerField(null=True, blank=True)
    subnet_mask = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)

class TableE(models.Model):
    first_octet = models.IntegerField(null=True, blank=True)
    second_octet = models.IntegerField(null=True, blank=True)
    third_octet = models.IntegerField(null=True, blank=True)
    fourth_octet = models.IntegerField(null=True, blank=True)
    subnet_mask = models.IntegerField(null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)

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
    column2 = models.CharField(max_length=255, null=True, blank=True)
    column3 = models.CharField(max_length=255, null=True, blank=True)
    column4 = models.CharField(max_length=255, null=True, blank=True)
    column5 = models.CharField(max_length=255, null=True, blank=True)
    column6 = models.CharField(max_length=255, null=True, blank=True)
    column7 = models.CharField(max_length=255, null=True, blank=True)
    column8 = models.CharField(max_length=255, null=True, blank=True)
    column9 = models.CharField(max_length=255, null=True, blank=True)
    column10 = models.CharField(max_length=255, null=True, blank=True)
    column11 = models.CharField(max_length=255, null=True, blank=True)
    column12 = models.CharField(max_length=255, null=True, blank=True)
    column13 = models.CharField(max_length=255, null=True, blank=True)
    column14 = models.CharField(max_length=255, null=True, blank=True)
    column15 = models.CharField(max_length=255, null=True, blank=True)
    column16 = models.CharField(max_length=255, null=True, blank=True)
    column17 = models.CharField(max_length=255, null=True, blank=True)
    


