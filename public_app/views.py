# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from classes.models import Classes
from students.models import Students
from teachers.models import TeacherClasses
from django.contrib.auth.models import User


# Create your views here.
class HomeView(TemplateView):
	"""docstring for HomeView"""

	template_name = "common/base.html"
	model = Classes

	
	def get_context_data(self, **kwargs):
		s_total = Students.objects.all().count()
		# t_total = User.objects.all().count()
		a  =  User.objects.filter(is_superuser=False).count()
		# count = Classes.objects.all()
		context = super(HomeView, self).get_context_data(**kwargs)
		context['total_students'] = s_total
		context['total_teachers'] =  a

		# context['classes'] = count
		return context
		
