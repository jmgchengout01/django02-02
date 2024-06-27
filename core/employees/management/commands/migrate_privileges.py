from django.core.management.base import BaseCommand
from django.db import transaction
from privileges.models import Privilege


class Command(BaseCommand):
    help = 'Reset and repopulate data - Priveleges'

    def handle(self, *args, **kwargs):
        self.stdout.write('Clearing existing data...')
        Privilege.objects.all().delete()

        self.stdout.write('Populating data...')
        self.populate_data()

        self.stdout.write(self.style.SUCCESS(
            'Data reset and repopulated successfully.'))

    @transaction.atomic
    def populate_data(self):
        Privilege.objects.create(name='Add Employee')
        Privilege.objects.create(name='Edit Employee')
        Privilege.objects.create(name='Delete Employee')
