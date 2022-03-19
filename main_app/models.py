from django.db import models
from django.urls import reverse

class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    miles = models.IntegerField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})