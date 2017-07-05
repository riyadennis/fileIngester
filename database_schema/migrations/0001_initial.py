# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=50)),
                ('store_id', models.IntegerField(max_length=50)),
                ('is_promotion', models.BooleanField(default=False)),
                ('sku', models.CharField(max_length=50)),
            ],
        ),
    ]
