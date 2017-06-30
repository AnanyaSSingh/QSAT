# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20160623_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='city',
            field=models.CharField(max_length=120, choices=[('Vadodara', 'Vadodara'), ('Ahmedabad', 'Ahmedabad'), ('Amravati', 'Amravati'), ('Aurangabad', 'Aurangabad'), ('Bangalore', 'Bangalore'), ('Bhopal', 'Bhopal'), ('Indore', 'Indore'), ('Jodhpur', 'Jodhpur'), ('Pune', 'Pune'), ('Raipur', 'Raipur'), ('Trivandrum', 'Trivandrum')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='level',
            field=models.CharField(max_length=120, choices=[('9-10', '9th or 10th Standard'), ('11-12', '11th or 12th Standard')]),
        ),
    ]
