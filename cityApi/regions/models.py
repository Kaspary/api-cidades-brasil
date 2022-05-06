from django.db import models
from cityApi.core.models import BaseModel


class State(BaseModel):
    code_uf = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)
    uf = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name + ' - ' + self.uf

class City(BaseModel):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    code_ibge = models.CharField(max_length=50, unique=True)
    capital = models.BooleanField(default=False)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' - ' + self.state.uf