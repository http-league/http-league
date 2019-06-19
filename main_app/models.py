from django.db import models
from django.urls import reverse
from datetime import date, datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Style(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Tech_stack(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name



class Site(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    tech_stack = models.ForeignKey(Tech_stack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # Assigning a specific site to a user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    class Meta:
        ordering = ('-pub_date',)

class Photo(models.Model):
    url = models.CharField(max_length=200)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    # submission = models.ManyToManyField(Submission)

    def __str__(self):
        return f"Photo for site_id: {self.site_id} @{self.url}"


class Submission(models.Model):
    site_name = models.CharField(max_length=100)
    URL = models.CharField(max_length=200)
    statement = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    tech_stack = models.ForeignKey(Tech_stack, on_delete=models.CASCADE)
    photo = models.ManyToManyField(Photo)

    def __str__(self):
        return self.statement


class Comment(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='comments')
    username = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by: {}'.format(self.username)

    class Meta:
        ordering = ['-created',]






# class Blog(models.Model):


# class User(models.Model):
