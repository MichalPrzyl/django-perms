from django.core.management.base import BaseCommand, CommandError
from user.models import Permission


class Command(BaseCommand):
    help = "Prints all permissions"


    def handle(self, *args, **options):
        print(f"\n\nPRINTING PERMISSIONS\n\n")

        permissions = Permission.objects.all()

        for permission in permissions:
            print(f"name: {permission.name}, model: {permission.model}, role: {permission.role}")
            print(f"READ: {permission.read}")
            print(f"WRITE: {permission.write}")
            print(f"DELETE: {permission.delete}")
            print(100*'-')
