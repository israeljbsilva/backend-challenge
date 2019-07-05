import factory
from django.contrib.auth.hashers import make_password

from ..models import Person, Pet

from django.contrib.auth.models import User


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


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('123456'))
    is_staff = True
    is_superuser = True
