from django.contrib import admin
from django.forms import ModelForm

from .models import Registration, Owner, Pet, Breed


class RegistrationForm(ModelForm):
    pass


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    """Регистрационные документы"""
    exclude = ["reg_num"]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    """Владелец питомца"""
    exclude = ["firstname", "lastname"]


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass

