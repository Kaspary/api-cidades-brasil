from django.db import models

class State(models.Model):
    code_uf = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50, unique=True)
    uf = models.CharField(max_length=2, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.uf

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    code_ibge = models.CharField(max_length=50, unique=True)
    capital = models.BooleanField(default=False)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + ' - ' + self.state.uf