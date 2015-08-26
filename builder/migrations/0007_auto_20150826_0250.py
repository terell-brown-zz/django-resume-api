# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0006_auto_20150809_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='resume_id',
            field=models.ForeignKey(related_name='about', default=-1, to='builder.Resume'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='resume_id',
            field=models.ForeignKey(related_name='contact', default=-1, to='builder.Resume'),
        ),
        migrations.AlterField(
            model_name='education',
            name='resume_id',
            field=models.ForeignKey(related_name='education', default=-1, to='builder.Resume'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='work_id',
            field=models.ForeignKey(related_name='experience', to='builder.Work'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='user',
            field=models.ForeignKey(related_name='resumes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='skill',
            name='resume_id',
            field=models.ForeignKey(related_name='skill', default=-1, to='builder.Resume'),
        ),
        migrations.AlterField(
            model_name='work',
            name='resume_id',
            field=models.ForeignKey(related_name='work', default=-1, to='builder.Resume'),
        ),
    ]
