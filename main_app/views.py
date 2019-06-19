from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


from datetime import datetime
# from .form import *
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm

from .models import *

# Create your views here.


today = datetime.today()
year = datetime.now().year


class SiteCreate(CreateView):
    model = Site
    fields = '__all__'

    # this
    def form_valid(self, form):
        # assigned the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the form work as normal
        return super().form_valid(form)

# Class SiteUpdate(UpdateView)
# TODO: Add Submission Create
# TODO: Add Submission Update
# TODO: Add Submission Delete

# TODO: Add Comment Create
# TODO: Add Comment Update
    # * Class based View
# TODO: Add Comment Delete
    # * Class based View

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
