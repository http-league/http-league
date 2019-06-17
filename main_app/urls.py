from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('category/<int:category_id>/', views.category_detail, name='category'),
    path('sites/<int:sites_id>/', views.sites_detail, name='detail'),
]
