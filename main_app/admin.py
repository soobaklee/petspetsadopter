from django.contrib import admin
from .models import Pet, Energy, Home, Photo

# Register your models here.
admin.site.register(Pet)
admin.site.register(Energy)
admin.site.register(Home)
admin.site.register(Photo)