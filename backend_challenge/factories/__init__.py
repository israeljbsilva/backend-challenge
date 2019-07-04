import factory

from ..models import Person, Pet


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    id = 1
    name = 'Israel'


class PetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pet

    id = 1
    name = 'Fred'
    person = factory.SubFactory(PersonFactory)
