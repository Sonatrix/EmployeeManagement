# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 07:29
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('fax', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(max_length=255)),
                ('added_date', models.DateField(auto_now=True)),
                ('added_by', models.IntegerField()),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(default=0)),
                ('company_name', models.CharField(max_length=255)),
                ('company_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('is_company', models.BooleanField()),
                ('is_contact', models.BooleanField()),
                ('added_date', models.DateField(auto_now=True)),
                ('added_by', models.IntegerField()),
                ('deleted', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CompanyServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('server_os', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
                ('server_name', models.CharField(max_length=255)),
                ('public_ip', models.CharField(max_length=100)),
                ('private_ip', models.CharField(max_length=100)),
                ('alert_sender_email1', models.EmailField(max_length=100)),
                ('alert_sender_email2', models.EmailField(blank=True, max_length=100)),
                ('alert_sender_email3', models.EmailField(blank=True, max_length=100)),
                ('escalate_to_email1', models.EmailField(max_length=100)),
                ('escalate_to_email2', models.EmailField(blank=True, max_length=100)),
                ('added_date', models.DateField(auto_now=True)),
                ('added_by', models.IntegerField()),
                ('deleted', models.IntegerField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autotriage.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=250)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(blank=True, max_length=240, null=True)),
                ('added_date', models.DateField(auto_now=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autotriage.Branch')),
            ],
        ),
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
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('designation', models.CharField(max_length=100)),
                ('inserted_by', models.BigIntegerField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Autotriage.Company'),
        ),
    ]
