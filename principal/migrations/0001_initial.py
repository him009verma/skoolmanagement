# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-12 10:52
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(code='invalid_first_name', message='Name must be Alphabetic', regex='^[a-zA-Z]*$')])),
                ('dob', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')])),
                ('picture', models.ImageField(blank=True, default='principal/img/default.png', height_field='height_field', null=True, upload_to='', verbose_name='profile picture', width_field='width_field')),
                ('height_field', models.IntegerField(default=600, null=True)),
                ('width_field', models.IntegerField(default=600, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
