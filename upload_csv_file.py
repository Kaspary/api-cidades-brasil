import csv
from core.models import *

with open('State.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:

        State.objects.create(code_uf=row[0],uf=row[1],name=row[2])

with open('City.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        City.objects.create(code_ibge=row[0],name=row[1],latitude=row[2],longitude=row[3],capital=True if row[4] == 1 else False,state=State.objects.get(code_uf=row[5]))
