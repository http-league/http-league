from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Site(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    pub_date =  models.DateField('publish date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # category = 
    # style = 
    # tech-stack = 

    def __str__(self):
        return self.name

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # def get_absolute_url(self):
    #   return reverse('______detail', kwargs={'pk': self.id})    


####MODELS####

#photo, category, style, tech-stack

class Submission(models.Model):
    statement = models.TextField(max_length=500)
    site_name = models.TextField(max_length=50)
    url = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.statement

    # def get_absolute_url(self):
    #   return reverse('______detail', kwargs={'pk': self.id})


class Comment(models.Model):
  date = models.DateField('comment date')
  txt_input = models.TextField(max_length=200)

  site = models.ForeignKey(Site, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.comment_display()} on {self.date}"

  class Meta:
    ordering = ['date']



