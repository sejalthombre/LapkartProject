from django.db import models

class Laptop(models.Model):
    company_name=models.CharField(max_length=32)
    model_name=models.CharField(max_length=32)
    ram = models.IntegerField()
    rom = models.IntegerField()
    price=models.FloatField()

