# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-01-14 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brambling', '0057_auto_20190105_0626'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DwollaAccount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dwolla_account',
        ),
        migrations.RemoveField(
            model_name='order',
            name='dwolla_test_account',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='dwolla_account',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='dwolla_test_account',
        ),
        migrations.RemoveField(
            model_name='person',
            name='dwolla_account',
        ),
        migrations.RemoveField(
            model_name='person',
            name='dwolla_test_account',
        ),
    ]
