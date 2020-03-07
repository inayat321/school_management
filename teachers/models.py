# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from classes.models import Classes

# Create your models here.

class TeacherClasses( models.Model):
	teacher = models.ForeignKey(User, on_delete=models.DO_NOTHING)
	teacher_class = models.ForeignKey(Classes, on_delete=models.DO_NOTHING)

	def __str__(self):
		return self.teacher.username


	