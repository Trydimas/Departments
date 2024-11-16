from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='subdepartments')


class Position(models.Model):
    title = models.CharField(max_length=255)
    department = models.ForeignKey(Department, related_name='positions', on_delete=models.CASCADE)


class Permission(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    departments = models.ManyToManyField(Department, related_name='employees')
    positions = models.ManyToManyField(Position, related_name='employees')
    permissions = models.ManyToManyField(Permission, related_name='employees')
