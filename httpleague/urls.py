f"""httpleague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from main_app import views
from main_app import views as user_views

urlpatterns = [
    path('', include('main_app.urls')),
    path('design/', include('design_system.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),

    # path('profile', user_views.profile, name='profile')
    # path('login', auth_views.LoginView.as_view(template_name='registration/login.html'). name='login')
    # path('logout', auth_views.LogoutView.as_view(template_name='registration/logout.html'). name='logout')
]
