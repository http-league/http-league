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
    name = models.CharField(max_length=50)
    pub_date =  models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)
    tech_stack = models.ForeignKey(Tech_stack, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_absolute_url(self):
    #   return reverse('______detail', kwargs={'pk': self.id})    


class Submission(models.Model):
    statement = models.TextField(max_length=500)
    site_name = models.TextField(max_length=50)
    url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    style = models.ManyToManyField(Style)
    tech_stack = models.ManyToManyField(Tech_stack)

    def __str__(self):
        return self.statement

    # def get_absolute_url(self):
    #   return reverse('______detail', kwargs={'pk': self.id})


class Comment(models.Model):
  date = models.DateTimeField(default=datetime.now())
  txt_input = models.TextField(max_length=200)

  site = models.ForeignKey(Site, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.comment_display()} on {self.date}"

  class Meta:
    ordering = ['date', 'author']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    submission = models.ManyToManyField(Submission)

    def __str__(self):
        return f"Photo for site_id: {self.site_id} @{self.url}"