from django.db import models

class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    miles = models.IntegerField()

    def __str__(self):
        return self.brand
