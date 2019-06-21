
from django.forms import ModelForm

from .models import *

class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url',
                'category', 'style', 'tech_stack']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'url': forms.URLInput(attrs={'class': 'input', 'value':'https://'}),
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
