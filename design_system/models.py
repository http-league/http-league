from django.db import models
from django.urls import reverse

from django.template.defaultfilters import slugify
# Create your models here.


class Component(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=15)
    description = models.TextField()
    example_code = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Component, self).save(*args, **kwargs)


class Utility(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=15)
    description = models.TextField()
    example_code = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Utility, self).save(*args, **kwargs)
