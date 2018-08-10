# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-10 16:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('date_published', models.DateTimeField(default=datetime.datetime.now)),
                ('post_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user_who_published',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud_app.User'),
        ),
    ]
