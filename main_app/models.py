from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.CharField(max_length=100)
    species = models.CharField(max_length=150)
    common_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    height = models.IntegerField()
    weight = models.IntegerField()
    intro = models.TextField(max_length=300)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})

class Nutrition(models.Model):