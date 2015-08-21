# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0004_education_gpa'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='resume_id',
            field=models.ForeignKey(default=-1, to='builder.Resume'),
        ),
    ]
