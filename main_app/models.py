from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

ENERGY_SOURCES = (
    ('F', 'Food'),
    ('W', 'Water'),
    ('S', 'Snack'),
    ('L', 'Sunlight'),
)

class Necessity(models.Model):
    item = models.CharField(max_length=50)
    color = models.CharField(max_length=40)

    def __str__(self):
        return self._check_column_name_clashes

    def get_absolute_url(self):
        return reverse('necessities_detail', kwarts={'pk': self.id})


class Pet(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.CharField(max_length=100)
    species = models.CharField(max_length=150)
    common_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    height = models.IntegerField('Height (in)')
    weight = models.IntegerField('Weight (lbs)')
    intro = models.TextField(max_length=300)
    heaven = models.BooleanField(default=False)
    necessities = models.ManyToManyField(Necessity)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id': self.id})

    def add_energy(request, pet_id):
        form = EnergyForm(request.POST)
        if form.is_valid():
            new_energy

    def energized_infull(self):
        return self.energy_set.filter(date=date.today()).count() >= 2

class Energy(models.Model):
    date = models.DateTimeField()
    energy_source = models.CharField(
        max_length=1,
        choices=ENERGY_SOURCES,
        default=ENERGY_SOURCES[0][0]  
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_energy_source_display()} on {self.date}"

    class Meta:
        ordering = ['-date']
    