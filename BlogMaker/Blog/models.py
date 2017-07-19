from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Blog(models.Model):
    owner = models.ForeignKey(User, default=0)
    blog_id = models.AutoField(primary_key='true')
    name = models.CharField(max_length=50)
    time = models.DateField(auto_now_add='true')

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post_id = models.AutoField(primary_key='true')
    summary = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=350)
    time = models.DateField(auto_now_add='true')

    def __str__(self):
        return str(self.summary)

    @staticmethod
    def create(blog, title, summary, text):
        return Post.objects.create(blog=blog, title=title, summary=summary, text=text)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    time = models.DateField(auto_now_add='true')

    def __str__(self):
        return str(self.text)

    @staticmethod
    def create(post, text):
        return Comment.objects.create(post=post, text=text)
