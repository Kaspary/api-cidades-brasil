from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import StateSerializer, CitySerializer
from .models import *



class StateList(generics.ListAPIView):
    
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


class StateDetail(generics.RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', '=code_ibge', 'state__name')


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer