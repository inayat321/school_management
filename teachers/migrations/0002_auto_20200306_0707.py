# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-06 07:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('teacher_class', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.Classes')),
            ],
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='teachers',
            name='teacher_class',
        ),
        migrations.DeleteModel(
            name='Teachers',
        ),
    ]
