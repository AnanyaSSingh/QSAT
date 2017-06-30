# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_register_roll'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='payed',
        ),
        migrations.RemoveField(
            model_name='register',
            name='receipt',
        ),
        migrations.RemoveField(
            model_name='register',
            name='roll',
        ),
    ]
