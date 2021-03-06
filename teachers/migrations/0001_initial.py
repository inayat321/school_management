# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-04 10:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_teacher', to=settings.AUTH_USER_MODEL)),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teachers', to='classes.Classes')),
            ],
        ),
    ]
