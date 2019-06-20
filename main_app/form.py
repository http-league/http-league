from django import forms

from .models import *


class SubmissionForm(forms.Form, forms.ModelForm):
    file_field = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta:
        model = Submission
        fields = ['site_name', 'url', 'statement',
                  'category', 'style', 'tech_stack']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('username', 'body')
