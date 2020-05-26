"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .forms import contactForm, CommentForm, BlogForm
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import Blog
from .models import Comment


def home(request):
  """Renders the home page."""
  assert isinstance(request, HttpRequest)
  return render(
    request,
    'app/index.html',
    {
      'title':'Home Page'
    }
  )

def contact(request):
  """Renders the contact page."""
  assert isinstance(request, HttpRequest)
  data = None
  if request.method == 'POST':
    form = contactForm(request.POST)
    if form.is_valid():
      data = dict()
      data['name'] = form.cleaned_data['name']
      data['email'] = form.cleaned_data['email']
      data['message'] = form.cleaned_data['message']
      form = None
  else:
    form = contactForm()
  return render(
    request,
    'app/contact.html',
    {
      'form': form,
      'data': data
    }
  )

def about(request):
  """Renders the about page."""
  assert isinstance(request, HttpRequest)
  return render(
    request,
    'app/about.html',
    {
      'title':'About',
      'message':'Your application description page.'
    }
  )

def registration(request):
  """Renders the redistration page."""
  if request.method == "POST":
    regform = UserCreationForm(request.POST)
    if regform.is_valid():
      reg_f = regform.save(commit=False)
      reg_f.is_staff = False
      reg_f.is_active = True
      reg_f.is_superuser = False
      reg_f.date_joinded = datetime.now()
      reg_f.last_login = datetime.now()
      regform.save()
      return redirect('home')
  else:
    regform = UserCreationForm()
  
  assert isinstance(request, HttpRequest)
  return render(
    request,
    'app/registration.html',
    {
      'regform': regform
    }
  )

def blog(request):
  """ """
  posts = Blog.objects.all()

  if request.method == "POST":
    form = BlogForm(request.POST)
    if form.is_valid():
      post_f = form.save(commit=False)
      post_f.save()
      return redirect('blog')
  else:
    form = BlogForm()

  assert isinstance(request, HttpRequest)
  return render(
    request,
    "app/blog.html",
    {
      'title': 'Blog',
      'form': form,
      'posts': posts
    }
  )

def blogpost(request, postnum):
  """ """
  post = Blog.objects.get(id=postnum)
  comments = Comment.objects.filter(post=postnum)

  if request.method == "POST":
    form = CommentForm(request.POST)
    if form.is_valid():
      comment_f = form.save(commit=False)
      comment_f.author = request.user
      comment_f.date = datetime.now()
      comment_f.post = Blog.objects.get(id=postnum)
      comment_f.save()

      return redirect('blogpost', postnum=post.id)
  else:
    form = CommentForm()
  
  assert isinstance(request, HttpRequest)
  return render(
    request,
    "app/blogpost.html",
    {
      'post': post,
      'comments': comments,
      'form': form
    }
  )