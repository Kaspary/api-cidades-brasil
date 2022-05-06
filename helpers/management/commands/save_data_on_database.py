import csv
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from cityApi.regions.models import State, City

class Command(BaseCommand):

    help = 'Command to save data on database'

    STATES_FILE = 'helpers/management/commands/data/state.csv'
    CITIES_FILE = 'helpers/management/commands/data/city.csv'

    def _read_csv(self, filename):
        with open(filename, mode='r', encoding='utf-8-sig') as csv_file:
            return list(csv.DictReader(csv_file, delimiter=','))


    def _get_states(self):
        return self._read_csv(self.STATES_FILE)
    
    def _get_cities(self):
        return self._read_csv(self.CITIES_FILE)
    
    def _save_states(self):
        try:
            State.objects.bulk_create([State(**d) for d in self._get_states()])
        except IntegrityError:
            pass
    
    def _save_cities(self):
        try:
            City.objects.bulk_create(
                [City(state=State.objects.get(code_uf=d.pop('state')), **d) for d in self._get_cities()]
            )
        except IntegrityError:
            pass

    def handle(self, *args, **kwargs):
        self._save_states()
        self._save_cities()

        



 