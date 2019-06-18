from django.contrib import admin
from .models import Site, Category, Tech_stack, Style

# Register your models here.

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Tech_stack)
# admin.site.register(Submission)
