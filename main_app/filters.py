from .models import Pet
import django_filters


class PetFilter(django_filters.FilterSet):
    class Meta:
        model = Pet
        fields = ['name', 'kingdom', 'common_name']

