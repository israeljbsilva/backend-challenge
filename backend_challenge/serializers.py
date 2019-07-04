from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from .models import Person, Pet


class PersonSerializer(ModelSerializer):
    resource_uri = HyperlinkedIdentityField(view_name='backend_challenge:person-detail')

    class Meta:
        model = Person
        fields = ('id', 'name', 'resource_uri',)


class PetSerializer(ModelSerializer):
    resource_uri = HyperlinkedIdentityField(view_name='backend_challenge:pet-detail')

    class Meta:
        model = Pet
        fields = ('id', 'name', 'resource_uri', 'person',)


class PetListSerializer(PetSerializer):
    person = PersonSerializer(read_only=True)
