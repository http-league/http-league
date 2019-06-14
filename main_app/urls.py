from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
]
