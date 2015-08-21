# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('career', models.CharField(max_length=50)),
                ('about_me', models.TextField()),
                ('photo', models.ImageField(upload_to=b'')),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('website', models.URLField()),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree_type', models.CharField(max_length=100)),
                ('program', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('proficiency', models.IntegerField(default=0)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_type', models.CharField(max_length=30)),
                ('organization', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=30)),
                ('province', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True)),
                ('skills_used', models.TextField()),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='experience',
            name='work_id',
            field=models.ForeignKey(to='builder.Work'),
        ),
    ]
