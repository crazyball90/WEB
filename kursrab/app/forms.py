"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Comment
from .models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
  """Authentication form which uses boostrap CSS."""
  username = forms.CharField(
    max_length=254,
    widget=forms.TextInput({
      'class': 'form-control',
      'placeholder': 'User name'}))

  password = forms.CharField(
    label=_("Password"),
    widget=forms.PasswordInput({
      'class': 'form-control',
      'placeholder':'Password'}))

class contactForm(forms.Form):
  """Contact form which uses boostrap CSS classes."""
  name = forms.CharField(
    label='Name',
    min_length=2,
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control'}))

  email = forms.EmailField(
    label='E-mail',
    widget=forms.TextInput(attrs={'class': 'form-control'}))

  message = forms.CharField(
    label='Message',
    widget=forms.Textarea(attrs={
        'rows': 12,
        'col': 20,
        'class': 'form-control'}))

class BlogForm(forms.ModelForm):
  class Meta:
    model = Blog
    fields = ('title', 'description', 'content',)
    labels = {'title': 'title', 'description': 'description', 'content': 'content'}

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('text',)
    labels = {'text': 'Comment'}