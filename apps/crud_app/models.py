from datetime import datetime

from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class Post(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    title = models.TextField()
    date_published = models.DateTimeField(default=datetime.now)
    user_who_published = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=False,
    )
    post_category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        primary_key=False,
    )
class Comment(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    corresponding_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_commented = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()
    date_published = models.DateTimeField(default=datetime.now)