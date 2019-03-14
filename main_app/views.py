from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pet
from .forms import EnergyForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def heaven(request):
    pets = Pet.objects.all()
    return render(request, 'pets/heaven.html', {'pets': pets})

def about(request):
    return render(request, 'about.html')

def pets_index(request):
    pets = Pet.objects.all()
    return render(request, 'pets/index.html', {'pets': pets})

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    energy_form = EnergyForm()
    return render(request, 'pets/detail.html', { 
        'pet': pet, 'energy_form': energy_form 
    })

def add_energy(request, pet_id):
    energy_form = EnergyForm(request.POST)
    if energy_form.is_valid():
        new_energy = energy_form.save(commit=False)
        new_energy.pet_id = pet_id
        new_energy.save()
    return redirect('detail', pet_id=pet_id)


class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'kingdom', 'species', 'common_name', 'birthday', 'height', 'weight', 'intro']
    success_url = '/pets/'

class PetUpdate(UpdateView):
    model = Pet
    fields = ['kingdom', 'species', 'common_name', 'birthday', 'height', 'weight']

class PetDelete(DeleteView):
    model = Pet
    success_url = '/pets/'

def send_heaven(request, pet_id):
    
    if heaven_form.is_valid():
        heaven.pet_id == True
    success_url = '/pets/heaven/'

