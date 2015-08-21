# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0003_auto_20150729_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='gpa',
            field=models.IntegerField(default=-1),
        ),
    ]
