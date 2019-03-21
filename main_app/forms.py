from django.forms import ModelForm
from .models import Energy, Pet, Home

class EnergyForm(ModelForm):
    class Meta:
        model = Energy
        fields = ['energy_source', 'date']

# class UserSignupForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'password', 'email']

class HeavenForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['heaven']

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ['style', 'size', 'color']
