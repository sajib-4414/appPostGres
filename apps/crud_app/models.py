from datetime import datetime

from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=15)

class Post(models.Model):
    title = models.TextField()
    date_published = models.DateTimeField(default=datetime.now)
    description = models.TextField()
    user_who_published = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    post_category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    image_file_link = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
class Comment(models.Model):
    corresponding_post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_commented = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.TextField()
    date_published = models.DateTimeField(default=datetime.now)