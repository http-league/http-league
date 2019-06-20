from django.db import models
from django.urls import reverse
from datetime import date, datetime

from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from django.apps import AppConfig

# Create your models here.


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=kwargs.get('instance'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=75)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'


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

    def get_absolute_url(self):
        return reverse('sites_detail', kwargs={'site_id': self.id})

    class Meta:
        ordering = ('-pub_date',)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for site_id: {self.site_id} @{self.url}"


class Submission(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    statement = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    tech_stack = models.ForeignKey(Tech_stack, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return self.statement

    def get_absolute_url(self):
        return reverse('submission_detail', kwargs={'submission_id': self.id})


class Comment(models.Model): 
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='comments')
    # ! TODO: CHANGE username field to 1:M relationship where a User has many comments.
    username = models.CharField(max_length=100)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by: {}'.format(self.username)

    def get_absolute_url(self):
        return reverse('comments_create', kwargs={'comment_id': self.id})

    class Meta:
        ordering = ['-created', ]


class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    body = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_fields = models.TextField()
    

class UserForm(ModelForm):
    username = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=40)
    last_name = forms.CharField(max_length=40)
    email = forms.EmailField(max_length=75)
    occupation = forms.CharField(max_length=40)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'occupation']