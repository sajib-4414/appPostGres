# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-11 12:46
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date_published', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date_published', models.DateTimeField(default=datetime.datetime.now)),
                ('description', models.TextField()),
                ('post_category', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
        migrations.AddField(
            model_name='comment',
            name='corresponding_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud_app.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_commented',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='crud_app.User'),
        ),
    ]
