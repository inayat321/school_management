# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Classes(models.Model):
	name = models.CharField(null=False,blank=False,max_length=15)

	def __str__(self):
		return self.name
