from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

# class Style(models.Model):
#     name = models.CharField(max_length=25)

#     def __str__(self):
#         return self.name


# class Tech_stack(models.Model):
#     name = models.CharField(max_length=25)

#     def __str__(self):
#         return self.name


class Site(models.Model):
    url = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    pub_date =  models.DateField('publish date')
    category = models.ManyToManyField(Category)
    # style = models.ForeignKey(Style, on_delete=models.CASCADE)
    # tech_stack = models.ForeignKey(Tech_stack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



# models
#submission, comment, photo, cetegory, style, tech-stack

# class Submission(Site):
#     statement = TextField(max_length=500)
    

