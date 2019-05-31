from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import State, City


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ('code_uf', 'name', 'uf')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'state', 'code_ibge', 'capital', 'latitude', 'longitude')