from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    read = models.TextField(null=True)
    write = models.TextField(null=True)
    delete = models.TextField(null=True)


