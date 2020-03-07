# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.detail import DetailView
from classes.models import Classes


class StudentListView(DetailView):
	"""docstring for ClassName"""

	template_name = "students/student_list.html"
	model = Classes

















# from django.shortcuts import render
# from django.views.generic.list import ListView
# from  students.models import  Students

# # Create your views here.
# class StudentListView(ListView):
# 	template_name = "students/student_list.html"
# 	model = Students
	
		