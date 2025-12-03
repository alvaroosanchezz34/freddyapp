from django.core.management.base import BaseCommand
from freddyapp.models import Animatronic, Party
from datetime import datetime


class Command(BaseCommand):
    help = 'Create sample animatronics and parties for testing'

    def handle(self, *args, **options):
        # Create parties
        parties_data = [
            {'name': 'Birthday Party', 'attendants': 20},
            {'name': 'Corporate Event', 'attendants': 50},
            {'name': 'Kids Party', 'attendants': 15},
        ]

        for party_data in parties_data:
            party, created = Party.objects.get_or_create(**party_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created party: {party.name}'))

        # Create animatronics
        animatronics_data = [
            {
                'name': 'Freddy Fazbear',
                'animal': 'BE',
                'build_date': datetime(2014, 1, 1).date(),
                'decommissioned': False,
            },
            {
                'name': 'Chica the Chicken',
                'animal': 'CH',
                'build_date': datetime(2014, 3, 15).date(),
                'decommissioned': False,
            },
            {
                'name': 'Bonnie the Bunny',
                'animal': 'BU',
                'build_date': datetime(2014, 2, 10).date(),
                'decommissioned': False,
            },
            {
                'name': 'Foxy the Pirate',
                'animal': 'FO',
                'build_date': datetime(2014, 6, 1).date(),
                'decommissioned': True,
            },
        ]

        for anim_data in animatronics_data:
            animatronic, created = Animatronic.objects.get_or_create(**anim_data)
            if created:
                # Add some parties
                parties = Party.objects.all()
                if parties.exists():
                    animatronic.parties.add(parties.first())
                self.stdout.write(self.style.SUCCESS(f'Created animatronic: {animatronic.name}'))

        self.stdout.write(self.style.SUCCESS('Sample data created successfully'))
