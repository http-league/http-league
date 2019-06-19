from django.urls import path
from . import views


urlpatterns = [
    # basic urls
    path('', views.index, name='design'),
    path('docs/', views.docs, name='docs'),
    path('docs/build-tools/', views.build_tools, name='build_tools'),


    # Component URLs

    path('docs/components/<slug:slug>/',
         views.components, name='components_detail '),

    # Utilities URLs
    path('docs/utilities/<slug:slug>/',
         views.utilities, name='utilities_detail'),

    # About URLs
    path('docs/about/', views.about, name='about'),
    path('docs/about/team/', views.about_team, name='about'),
]
