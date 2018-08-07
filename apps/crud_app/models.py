from django.db import models

# Create your models here.
from django import forms


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_number = models.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)