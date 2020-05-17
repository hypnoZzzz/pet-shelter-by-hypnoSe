import uuid
from django.utils.translation import gettext_lazy as _
from django.core import validators
from django.db import models
from django.urls import reverse


class Registration(models.Model):
    """Информация о регистрации питомца"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    date = models.DateField(verbose_name="Дата регистрации")
    cage = models.CharField(max_length=10, verbose_name=_("Номер клетки"))
    reg_num = models.CharField(max_length=256, auto_created=True,
                               null=True, blank=True,
                               verbose_name=_("Регистрационный номер"))

    def __str__(self):
        return self.reg_num if self.reg_num else self.date.strftime("%d-%m-%Y")


class Owner(models.Model):
    """Информация о владельце"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    firstname = models.CharField(max_length=256, verbose_name=_("Имя"))
    lastname = models.CharField(max_length=256, verbose_name=_("Фамилия"))
    note = models.CharField(max_length=256, verbose_name=_("Описание"))

    def __str__(self):
        return "{} {}".format(self.lastname, self.firstname)


class Breed(models.Model):
    """Описание породы"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=256,
                            verbose_name="Порода")
    code = models.CharField(max_length=256,
                            verbose_name="Код")

    def __str__(self):
        return self.name


class Pet(models.Model):
    """Информация о питомце"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    dog = 'DG'
    cat = 'CT'
    parrot = 'PR'

    animals = (
        (dog, 'собака'),
        (cat, 'кошка'),
        (parrot, 'попугай'),
    )
    type_of_animal = models.CharField(max_length=2, verbose_name="тип животного", choices=animals, default=dog)
    name = models.CharField(max_length=256, verbose_name="Кличка")
    age = models.IntegerField(verbose_name="Возраст",
                              validators=[validators.MaxValueValidator(100)])
    doc = models.ForeignKey('Registration', on_delete=models.CASCADE,
                            verbose_name="Регистрационный документ",
                            related_name="pet_registration")
    photo = models.ImageField(upload_to='pets_photo', blank=True)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE,
                              verbose_name="Порода")
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE,
                              verbose_name="Владелец", blank=True, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.doc.reg_num = self.breed.name[0] + self.doc.date.strftime(
            "%d%m%Y")
        self.doc.save()
        super().save()

    def make_word_end(self):
        word = "лет"
        n = self.age
        if n > 99:
            n = n % 100
        if n in range(5, 21):
            word = "лет"
        elif n % 10 == 1:
            word = "год"
        elif n % 10 in range(2, 5):
            word = "года"
        return "{} {}".format(self.age, word)

    def __str__(self):
        return "{} ({}, {})".format(self.name, self.breed,
                                    self.make_word_end())

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pk': self.pk})



