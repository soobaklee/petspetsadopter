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

SIZES = (
    ('T', 'Extra Small'),
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('X', 'Extra Large'),
    ('H', 'Huge'),
)

STYLES = (
    ('B', 'Blanket'),
    ('P', 'Pillow'),
    ('A', 'Apartment'),
    ('C', 'Condo'),
    ('H', 'House'),
    ('T', 'Aquarium'),
    ('L', 'Clay Pot'),
    ('V', 'Vase'),
    ('E', 'Petri Dish'),
)


class Pet(models.Model):
    name = models.CharField(max_length=100)
    kingdom = models.CharField(max_length=100)
    species = models.CharField(max_length=150)
    common_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    height = models.FloatField('Height (in)')
    weight = models.FloatField('Weight (lbs)')
    intro = models.TextField(max_length=300)
    heaven = models.BooleanField(default=False)
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
        return self.energy_set.filter(date=date.today()).count() >= 3

    def add_home(request, pet_id):
        form = HomeForm(request.POST)
        if form.is_valid():
            new_home

    def today_energy(self):
        current_date = date.today()
        return self.energy_set.filter(date=current_date)

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

    @property
    def is_today(self):
        print(self.date.strftime("%Y-%m-%d"))
        print(date.today())
        print(self.date.strftime("%Y-%m-%d") == date.today().strftime("%Y-%m-%d"))
        return self.date.strftime("%Y-%m-%d") == date.today().strftime("%Y-%m-%d")
        # return self.date == date.today()

    class Meta:
        ordering = ['-date']


class Home(models.Model):
    color = models.CharField(
        max_length=30,
        default='White',
    )
    style = models.CharField(
        max_length=1,
        choices=STYLES,
        default=STYLES[0][0]
    )
    size = models.CharField(
        max_length=1,
        choices=SIZES,
        default=SIZES[0][0]
    )
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"A {self.get_size_display()}, {self.color} {self.get_style_display()}"

    class Meta:
        ordering = ['style']

class Photo(models.Model):
    url = models.CharField(max_length=250)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id}, {self.pet.name} @ {self.url}"