# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0002_auto_20150729_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(default=b'', max_length=254)),
                ('phone_number', models.CharField(max_length=20, blank=True)),
                ('website', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('github', models.URLField(blank=True)),
                ('resume_id', models.ForeignKey(default=-1, to='builder.Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('skill_type', models.CharField(max_length=30)),
                ('proficiency', models.IntegerField(default=0)),
                ('resume_id', models.ForeignKey(default=-1, to='builder.Resume')),
            ],
        ),
        migrations.RemoveField(
            model_name='skills',
            name='resume_id',
        ),
        migrations.RemoveField(
            model_name='about',
            name='email',
        ),
        migrations.RemoveField(
            model_name='about',
            name='github',
        ),
        migrations.RemoveField(
            model_name='about',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='about',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='about',
            name='website',
        ),
        migrations.DeleteModel(
            name='Skills',
        ),
    ]
