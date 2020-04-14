from rest_framework import serializers
from .models import State, City


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =( 'code_uf', 'name', 'uf')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'state', 'code_ibge', 'capital', 'latitude', 'longitude')