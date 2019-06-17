from django.contrib import admin
from .models import Site, Submission, Comment

# Register your models here.

admin.site.register(Site)
admin.site.register(Submission)
admin.site.register(Comment)
