from django import forms
from .models import Post, CVItem


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CVItemForm(forms.ModelForm):
    class Meta:
        model = CVItem
        fields = ('author', 'title', 'text', 'priority',)
