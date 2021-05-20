from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name= models.CharField('Name',max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    color = models.CharField('Color', max_length=100)
    ram = models.IntegerField('RAM size in GBs')
    rom = models.IntegerField('ROM size in GBs')

    def __str__(self):
        return self.name
