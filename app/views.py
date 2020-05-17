
from django.views.generic.base import TemplateView
from django.views.generic import (ListView,
                                  DetailView)
from app.models import Pet


class IndexPageView(TemplateView):
    template_name = 'base/index.html'


class PetListView(ListView):
    model = Pet
    template_name = 'pets/pet_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        if get_params.get('q'):
            qs = qs.filter(breed__name=get_params.get('q'))

        return qs


class Cats:
    @staticmethod
    def get_cats():
        return Pet.objects.filter(type_of_animal='CT')


class CatListView(Cats, ListView):
    model = Pet
    template_name = 'pets/cat_list.html'


class Dogs:
    @staticmethod
    def get_dogs():
        return Pet.objects.filter(type_of_animal='DG')


class DogListView(Dogs, ListView):
    model = Pet
    template_name = 'pets/dog_list.html'


class Parrots:
    @staticmethod
    def get_parrots():
        return Pet.objects.filter(type_of_animal='PR')


class ParrotListView(Parrots, ListView):
    model = Pet
    template_name = 'pets/parrot_list.html'


class PetView(DetailView):
    model = Pet
    template_name = 'pets/pet_detail.html'






