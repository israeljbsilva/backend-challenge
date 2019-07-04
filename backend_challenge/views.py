import os

from django.http import JsonResponse
from django.utils import timezone

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Person, Pet
from .serializers import PersonSerializer, PetSerializer, PetListSerializer
from .pagination import DefaultPagination


def ping(request):
    return JsonResponse({
        'request': f'{request.environ.get("REQUEST_METHOD")} '
        f'{request.environ.get("HTTP_HOST")}{request.environ.get("PATH_INFO")}',
        'timestamp': timezone.localtime(),
        'build_date': os.environ.get('BUILD_DATE'),
        'revision': os.environ.get('REVISION')})


class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
    pagination_class = DefaultPagination
    permission_classes = (IsAuthenticated,)


class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    pagination_class = DefaultPagination
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        self.serializer_class = PetListSerializer
        return super().list(self, request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PetListSerializer
        return super().retrieve(self, request, *args, **kwargs)
