# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0002_auto_20180508_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapisy',
            name='your_choice',
            field=models.CharField(choices=[('Modern jazz', 'Modern jazz'), ('Modern balet', 'Modern balet'), ('Afro dance', 'Afro dance'), ('Break dance', 'Break dance')], max_length=1, null=True),
        ),
    ]
