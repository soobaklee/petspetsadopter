from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.http import HttpResponse, HttpRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .models import Pet, Home
from .forms import EnergyForm, HeavenForm, HomeForm
from .filters import PetFilter


# Create your views here.
def home(request):
    pets = Pet.objects.all()
    return render(request, 'home.html', {'pets': pets})

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
    home_form = HomeForm()
    return render(request, 'pets/detail.html', { 
        'pet': pet, 'energy_form': energy_form,
        'home_form': home_form,
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


def heaven_true(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    heaven_form = HeavenForm(request.POST)
    if heaven_form.is_valid():
        pet.heaven = True
        pet.save()
    return redirect('/pets/heaven/')

def send_heaven(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    heaven_form = HeavenForm()
    return render(request, 'pets/send_heaven.html', { 
        'pet': pet, 'heaven_form': heaven_form 
    })

def add_home(request, pet_id):
    home_form = HomeForm(request.POST)
    if home_form.is_valid():
        new_home = home_form.save(commit=False)
        new_home.pet_id = pet_id
        new_home.save()
    return redirect('detail', pet_id=pet_id)

def items_index(request):
    pets = Pet.objects.all()
    homes = Home.objects.all()
    return render(request, 'items/index.html', {'pets': pets, 'homes': homes})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid credentials - try again'
            
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
    
def pets_search(request):
    pet_list = Pet.objects.all()
    pet_filter = PetFilter(request.GET, queryset=pet_list)
    return render(request, 'pet_list.html', {'filter': pet_filter})


