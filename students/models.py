# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from classes.models import Classes


class Students(models.Model):
	name = models.CharField(null=False,blank=False,max_length=40)
	roll_no = models.PositiveIntegerField() 
	age =  models.PositiveIntegerField()
	student_class = models.ForeignKey(Classes,on_delete=models.DO_NOTHING, related_name="students")

	def __str__(self):
		return self.name
		
		

