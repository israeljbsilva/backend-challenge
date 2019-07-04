"""backend_challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from rest_framework_nested import routers

from .views import PersonViewSet, PetViewSet


app_name = 'backend_challenge'


persons_router = routers.DefaultRouter(trailing_slash=False)
persons_router.register(r'person', PersonViewSet)

pets_router = routers.DefaultRouter(trailing_slash=False)
pets_router.register(r'pet', PetViewSet)


urlpatterns = [
    path('', include(persons_router.urls)),
    path('', include(pets_router.urls)),
]
