from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


from datetime import datetime
# from .form import *
from .mixins import *
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

# Create your views here.


today = datetime.today()
year = datetime.now().year


def admin_check(user):
    return user.is_superuser

# // TODO: Site Class based views


class SiteCreate(isAdminMixin, CreateView):
    model = Site
    fields = '__all__'

    def form_valid(self, form):
        # assigned the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the form work as normal
        return super().form_valid(form)


class SiteUpdate(isAdminMixin, UpdateView):
    model = Site
    fields = '__all__'


class SiteDelete(isAdminMixin, UpdateView):
    model = Site
    success_url = '/'


# // TODO: Submission Class Based Views -- List, CD
class SubmissionList(ListView):
    model = Submission


class SubmissionCreate(LoginRequiredMixin, CreateView):
    model = Submission
    fields = '__all__'


class SubmissionDelete(isAdminMixin, DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Submission
    success_url = '/'


# ? TODO: Comment Class Based Views -- CUD


# TODO: Blog Post Class Based Views -- CRUD
class PostCreate(isAdminMixin, CreateView):
    model = Post


class PostList(ListView):
    model = Post


def home(request):
    return render(request, 'home.html', {'title': 'HTTP League · Web Design Repo', 'year': year})


def about(request):
    return render(request, 'about.html', {'title': 'About · HTTP League', 'year': year})


def blog_index(request):
    return render(request, 'blog/post_list.html', {'title': 'Blog · HTTP League', 'year': year})


def sites_detail(request):
    return render(request, 'sites/detail.html', {'title': 'HTTP League · Web Design Repo', 'year': year})


# def signup(request):
#     error_message = ''
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('index')
#         else:
#             error_message = 'Invalid sign up - try again'
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)
