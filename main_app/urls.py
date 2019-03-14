from django.urls import path
from django.views.generic.edit import CreateView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pets/heaven/', views.heaven, name="heaven"),
    path('about/', views.about, name="about"),
    path('pets/', views.pets_index, name="index"),
    path('pets/<int:pet_id>/', views.pets_detail, name="detail"),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/heaven/', views.send_heaven, name='send_heaven'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
    path('pets/<int:pet_id>/add_energy/', views.add_energy, name='add_energy'),

]