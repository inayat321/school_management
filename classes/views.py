# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from classes.models import Classes


# Create your views here.
class ClassListView(ListView):
	template_name ="classes/classes_list.html"
	model = Classes




	"""docstring for ClassListView"""
	

