from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


