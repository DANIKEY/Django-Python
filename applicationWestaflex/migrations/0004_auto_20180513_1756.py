# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-05-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationWestaflex', '0003_auto_20180513_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enregistreprocedure',
            name='id_procedure',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]