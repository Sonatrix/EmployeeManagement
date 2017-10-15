# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autotriage', '0010_auto_20171015_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('pop_server_name', models.CharField(blank=True, max_length=200)),
                ('pop_port', models.IntegerField()),
                ('imap_server_name', models.CharField(blank=True, max_length=200)),
                ('imap_port', models.IntegerField()),
                ('added_date', models.DateField(auto_now=True)),
                ('added_by', models.IntegerField()),
                ('deleted', models.IntegerField()),
            ],
        ),
    ]
