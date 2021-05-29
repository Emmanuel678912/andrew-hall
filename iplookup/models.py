from django.db import models

# Create your models here.
class TableA(models.Model):
    pass
class TableB(models.Model):
    pass

class TableC(models.Model):
    pass

class TableD(models.Model):
    first_octet = models.IntegerField()
    second_octet = models.IntegerField()
    third_octet = models.IntegerField()
    fourth_octet = models.IntegerField()
    subnet_mask = models.IntegerField()



class TableE(models.Model):
    first_octet = models.IntegerField()
    second_octet = models.IntegerField()
    third_octet = models.IntegerField()
    fourth_octet = models.IntegerField()
    subnet_mask = models.IntegerField()

class TableF(models.Model):
    first_octet = models.IntegerField()
    second_octet = models.IntegerField()
    third_octet = models.IntegerField()
    fourth_octet = models.IntegerField()
    subnet_mask = models.IntegerField()
    variable = models.IntegerField()

class TableG(models.Model):
    pass

class TableH(models.Model):
    pass

