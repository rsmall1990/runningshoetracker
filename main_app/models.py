from django.db import models
from django.urls import reverse

Runs = (
    ('L', 'Long'),
    ('S', 'Speed'),
    ('E', 'Easy'),
)

class Shoe(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    miles = models.IntegerField()

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'shoe_id': self.id})

class Run(models.Model):
    date = models.DateField()
    run = models.CharField(max_length=1, choices=Runs, default=[2][0])
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_run_display()} run on {self.date}"