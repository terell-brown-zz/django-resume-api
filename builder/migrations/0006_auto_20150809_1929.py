# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0005_experience_resume_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume',
            old_name='user_id',
            new_name='user',
        ),
    ]
