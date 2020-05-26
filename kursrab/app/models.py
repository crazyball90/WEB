"""
Definition of models.
"""

from django.db import models
from datetime import datetime
from django.contrib import admin
from django.urls  import reverse
from django.contrib.auth.models import User


class Blog(models.Model):
  title = models.CharField(max_length=100, unique_for_date="posted", verbose_name="Title")
  description = models.TextField(verbose_name="Description")
  content = models.TextField(verbose_name="Content")
  posted = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Posted")

  def get_absolute_url(self):
    return reverse("blogpost", args=[str(self.id)])
  
  def __str__(self):
    return self.title
  
  class Meta:
    db_table = "Posts"
    ordering = ["-posted"]
    verbose_name = "Blog page"
    verbose_name_plural = "Blog page"
  
admin.site.register(Blog)

class Comment(models.Model):
  text = models.TextField(verbose_name="Comment")
  date = models.DateTimeField(default=datetime.now(), db_index=True, verbose_name="Date")
  author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Author")
  post = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name="Post")

  def __str__(self):
    return 'Comment by %s for %s' % (self.author, self.post)
  
  class Meta:
    db_table = "Comments"
    verbose_name = "Comment"
    verbose_name_plural = "Blogposts comments"
    ordering = ["-date"]

admin.site.register(Comment)