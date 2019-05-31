from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, StateSerializer, CitySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import *


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'shema': reverse('shema', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'state': reverse('state-list', request=request, format=format),
        'city': reverse('city-list', request=request, format=format)
    })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StateList(generics.ListAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)


class StateDetail(generics.RetrieveAPIView):
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListAPIView):
    print("CITY")
    queryset = City.objects.all()
    serializer_class = CitySerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', '=code_ibge', 'state__name')


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer