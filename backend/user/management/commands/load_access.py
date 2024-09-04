from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import os, json
from user.models import Permission, Role
from django.apps import apps


class Command(BaseCommand):
    help = "Load all access files"


    def is_correct_field(self):
        pass

    def handle(self, *args, **options):

        with transaction.atomic():
            directory = os.fsencode('./access')

            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                # Ignore files other than *.access.
                if not filename.endswith(".access"): 
                    continue

                with open(f"./access/{filename}") as read_file:
                    lines = read_file.readlines()
                    # Remove comments.
                    filtered_lines = [line for line in lines if not line.strip().startswith("//")]
                    perm_obj = json.loads("\n".join(filtered_lines))

                    model = apps.get_model(perm_obj['model'])
                    fields = model._meta.get_fields()
                    fields_strings = [field.name for field in fields]
                    fields_strings.remove('id')
                    for role_permission in perm_obj['permissions']:

                        try:
                            role = Role.objects.get(name=role_permission['role'])
                        except Role.DoesNotExist:
                            # If role doesn't exist, just skip.
                            continue

                        # If role has full access to model's fields.
                        if role_permission['permissions'] == '__all__':
                            Permission.objects.update_or_create(
                                name=perm_obj['name'],
                                model=perm_obj['model'],
                                role=role,
                                defaults={
                                    'read': ", ".join(fields_strings),
                                    'write': ", ".join(fields_strings),
                                    'delete': ", ".join(fields_strings)
                                }
                            )

                        else:
                            x = role_permission['permissions']
                            Permission.objects.update_or_create(
                                name=perm_obj['name'],
                                model=perm_obj['model'],
                                role=role,
                                defaults={
                                    'read': ", ".join(role_permission['permissions'].get('read', [])),
                                    'write': ", ".join(role_permission['permissions'].get('write', [])),
                                    'delete': ", ".join(role_permission['permissions'].get('delete', []))
                                })
