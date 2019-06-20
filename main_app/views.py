from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import ListView, DetailView, View


from datetime import datetime
from .form import *
from .mixins import *
from django.contrib.auth import login
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid
import boto3
from .models import *
# Create your views here.

BUCKET = 'httpleague'
S3_BASE_URL = f'https://{BUCKET}.s3.amazonaws.com/'

today = datetime.today()
year = datetime.now().year


def admin_check(user):
    return user.is_superuser

# // TODO: Site Class based views


class SiteCreate(CreateView):
    model = Site
    fields = '__all__'

    def form_valid(self, form):
        # assigned the logged in user (self.request.user)
        form.instance.user = self.request.user
        # Let the form work as normal
        return super().form_valid(form)


class SiteUpdate(UpdateView):
    model = Site
    fields = '__all__'


class SiteDelete(UpdateView):
    model = Site
    success_url = '/'


# // TODO: Submission Class Based Views -- List, CD
class SubmissionList(ListView):
    model = Submission


class SubmissionCreate(FormView):
    model = Submission
    fields = '__all__'
    form_class = SubmissionForm
    template_name = 'main_app/submission_form.html'

    def post(self, request, submission_id, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('photo-files')
        if form.is_valid():
            for f in files:
                s3 = boto3.client('s3')
                key = uuid.uuid4().hex[:4] + f.name[f.name.rfind('.'):]
                try:
                    s3.upload_fileobj(f, BUCKET, key)
                    url = f"{S3_BASE_URL}{key}"
                    photo = Photo(url=url, submission_id=submission_id)
                    photo.save()
                except:
                    print('An error occurred uploading file to S3')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

        return redirect('submission_detail', submission_id=submission_id)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class SubmissionDelete(DeleteView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Submission
    success_url = '/'


# ? TODO: Comment Class Based Views -- CUD


# TODO: Blog Post Class Based Views -- CRUD
# class PostCreate(isAdminMixin, CreateView):
#     model = Post


# class PostList(ListView):
#     model = Post

# class PostUpdate(isAdminMixin, UpdateView):
#     model = Post
#     fields = '__all__'


# class PostDelete(isAdminMixin, DeleteView):
#     model = Post
#     success_url = '/blog/'

# TODO: FINISH home.html template
def home(request):
    return render(request, 'home.html', {'title': 'HTTP League · Web Design Repo', 'year': year})


# TODO: FINISH about.html template
def about(request):
    return render(request, 'about.html', {'title': 'About · HTTP League', 'year': year})


# TODO: FINISH post_list.html template
def blog_index(request):
    return render(request, 'blog/post_list.html', {'title': 'Blog · HTTP League', 'year': year})


# TODO: FINISH sites/detail.html
def sites_detail(request):
    return render(request, 'sites/detail.html', {'title': 'HTTP League · Web Design Repo', 'year': year})


def category_detail(request):
    return render(request, 'category/detail.html', {'title': 'Category · HTTP League', 'year': year})


def submissions_detail(request, submission_id):
    submission = Submission.objects.get(id=submission_id)

    return render(request, 'main_app/submission_detail.html', {'title': 'Submission · HTTP League', 'submission': submission, 'year': year})

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
