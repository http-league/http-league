
from django.forms import ModelForm

from .models import *

class SiteCreateForm(forms.ModelForm):
    class Meta:
        model = Site
        fields = ['name', 'url',
                'category', 'style', 'tech_stack']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'url': forms.URLInput(attrs={'class': 'input'}),
            'category': forms.SelectMultiple(attrs={'class': 'select-multiple'}),
            'style': forms.Select(attrs={'class': 'select'}),
            'tech_stack': forms.Select(attrs={'class': 'select'}),
        }

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('username', 'body')
