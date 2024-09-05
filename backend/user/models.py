from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    model =models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    read = models.TextField(null=True)
    write = models.TextField(null=True)
    delete = models.TextField(null=True)


class User(AbstractBaseUser):
    roles = models.ManyToManyField('user.Role', through='user.UserRole', blank=True, related_name='role_users')


class UserRole(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    role = models.ForeignKey('user.Role', on_delete=models.CASCADE)
