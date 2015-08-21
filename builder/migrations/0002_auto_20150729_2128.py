# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('context', models.CharField(max_length=30)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='about',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='education',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='skills',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='work',
            name='user_id',
        ),
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(default=b'', max_length=254),
        ),
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='phone_number',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='about',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='about_me',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='about',
            name='photo',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
        migrations.AddField(
            model_name='about',
            name='resume_id',
            field=models.ForeignKey(default=-1, to='builder.Resume'),
        ),
        migrations.AddField(
            model_name='education',
            name='resume_id',
            field=models.ForeignKey(default=-1, to='builder.Resume'),
        ),
        migrations.AddField(
            model_name='skills',
            name='resume_id',
            field=models.ForeignKey(default=-1, to='builder.Resume'),
        ),
        migrations.AddField(
            model_name='work',
            name='resume_id',
            field=models.ForeignKey(default=-1, to='builder.Resume'),
        ),
    ]
