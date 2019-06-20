from django.contrib import admin

from .models import Site, Category, Style, Tech_stack, Submission, Comment, Photo, Profile, Post

# Register your models here.

admin.site.register(Profile)
admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Tech_stack)
admin.site.register(Submission)
admin.site.register(Photo)
admin.site.register(Comment)
admin.site.register(Post)


