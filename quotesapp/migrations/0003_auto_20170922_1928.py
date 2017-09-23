# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0002_auto_20170913_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='text',
            field=models.TextField(max_length=500),
        ),
    ]
