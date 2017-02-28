# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-20 19:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='base_price',
            field=models.DecimalField(max_digits=18, decimal_places=2,
                                      verbose_name=_('base price')),
        ),
    ]
