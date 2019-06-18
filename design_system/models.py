from django.db import models
from django.urls import reverse
# Create your models here.


class Component(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    example_code = models.TextField()

    def __str__(self):
        return self.name


class Utility(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    example_code = models.TextField()

    def __str__(self):
        return self.name
