from django.core.management.base import BaseCommand
from tables.models import Table

class Command(BaseCommand):
    help = 'Adds a table to the database'

    def handle(self, *args, **kwargs):
        # Clear existing tables
        Table.objects.all().delete()

        # Add new talbes
        tables_data = [
            {'number': 1, 'capacity': 4},
            {'number': 2, 'capacity': 6},
            {'number': 3, 'capacity': 2},
            {'number': 4, 'capacity': 2},
            {'number': 5, 'capacity': 4},
            {'number': 6, 'capacity': 4},
            {'number': 7, 'capacity': 6},
            {'number': 8, 'capacity': 6},
            {'number': 9, 'capacity': 8},
        ]

        for data in tables_data:
            Table.objects.create(**data)

        self.stdout.write(self.style.SUCCESS('Tables data added successfully'))
