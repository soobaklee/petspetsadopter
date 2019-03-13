from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pets_index(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'pets/detail.html', { 'pet': pet })

class PetCreate(CreateView):
    model = Pet
    fields = '__all__'
    success_url = '/pets/'

class PetUpdate(UpdateView):
    model = Pet
    fields = ['kingdom', 'species', 'common_name', 'birthday', 'height', 'weight']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/cats/'
