
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

from .models import *


class UserFullForm(UserCreationForm):
     # declare the fields you will show
    username = forms.CharField(label="Username")
    first_name = forms.CharField(label="Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")
    occupation = forms.CharField(label="Occupation")
    # first password field
    password1 = forms.CharField(label="Password")
    # confirm password field
    password2 = forms.CharField(label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'occupation']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
            return user


class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url',
                  'category', 'style', 'tech_stack']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'url': forms.URLInput(attrs={'class': 'input', 'value': 'https://'}),
            'category': forms.SelectMultiple(attrs={'class': 'select-multiple'}),
            'style': forms.Select(attrs={'class': 'select'}),
            'tech_stack': forms.Select(attrs={'class': 'select'}),
        }


class SubmissionCreateForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['site_name', 'url', 'statement',
                  'category', 'style', 'tech_stack']
        widgets = {
            'site_name': forms.TextInput(attrs={'class': 'input'}),
            'url': forms.URLInput(attrs={'class': 'input', 'value': 'https://'}),
            'statement': forms.Textarea(attrs={'class': 'input'}),
            'category': forms.SelectMultiple(attrs={'class': 'select-multiple'}),
            'style': forms.Select(attrs={'class': 'select'}),
            'tech_stack': forms.Select(attrs={'class': 'select'}),
        }
# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('username', 'body')
