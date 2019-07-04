from django.db import models
from django.db.models.fields import CharField
from django_extensions.db.models import TimeStampedModel


class Person(TimeStampedModel):
    name = CharField('NAME', max_length=256, null=False)

    class Meta:
        db_table = 'PERSON'
        verbose_name = 'person'
        verbose_name_plural = 'persons'


class Pet(TimeStampedModel):
    name = CharField('NAME', max_length=256, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    class Meta:
        db_table = 'PET'
        verbose_name = 'pet'
        verbose_name_plural = 'pets'
