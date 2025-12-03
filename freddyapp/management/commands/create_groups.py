from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from freddyapp.models import Animatronic


class Command(BaseCommand):
    help = 'Create Client and Staff groups with their permissions'

    def handle(self, *args, **options):
        # Get the Animatronic content type
        animatronic_ct = ContentType.objects.get_for_model(Animatronic)

        # Get all permissions for Animatronic
        view_perm = Permission.objects.get(content_type=animatronic_ct, codename='view_animatronic')
        add_perm = Permission.objects.get(content_type=animatronic_ct, codename='add_animatronic')
        change_perm = Permission.objects.get(content_type=animatronic_ct, codename='change_animatronic')
        delete_perm = Permission.objects.get(content_type=animatronic_ct, codename='delete_animatronic')

        # Create Client group with view permission
        client_group, created = Group.objects.get_or_create(name='Client')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Client group'))
        else:
            self.stdout.write('Client group already exists')

        client_group.permissions.set([view_perm])
        self.stdout.write(self.style.SUCCESS('Assigned view permission to Client group'))

        # Create Staff group with all permissions
        staff_group, created = Group.objects.get_or_create(name='Staff')
        if created:
            self.stdout.write(self.style.SUCCESS('Created Staff group'))
        else:
            self.stdout.write('Staff group already exists')

        staff_group.permissions.set([view_perm, add_perm, change_perm, delete_perm])
        self.stdout.write(self.style.SUCCESS('Assigned all permissions to Staff group'))

        self.stdout.write(self.style.SUCCESS('Successfully created groups and permissions'))
