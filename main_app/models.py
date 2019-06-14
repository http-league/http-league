from django.db import models
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


# models
#submission, comment, photo, cetegory, style, tech-stack

# class Submission(Site):
#     statement = TextField(max_length=500)
    

