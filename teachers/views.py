from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from teachers.models import TeacherClasses
from django.contrib.auth.models import User
# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'teachers/dashboard.html'
	login_url = '/teacher/login/'

	def get_context_data(self, **kwargs):
		context = super(DashboardView, self).get_context_data(**kwargs)
		teacher = self.request.user
		teachersclassesObjects = TeacherClasses.objects.filter(teacher = teacher)
		context['teacher_classes'] = teachersclassesObjects


		return context


class LoginView(View): 

	template_name = 'teachers/login.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)

	def post(self, request, *args, **kwargs):
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)

		user = authenticate(request, username=username, password=password)
		if user is not None:
			if  user==User.objects.filter(is_superuser=False):
				login(request, user)
				link = reverse('teachers:dashboard')
				return redirect(link)
			else:
				return render(request, self.template_name, {"msg": "Invalid Credentials"})


class LogoutView(View): 

	def get(self, request, *args, **kwargs):
		logout(request)
		link = reverse('teachers:login_page')
		return redirect(link)

class PasswordView(View):
	template_name = 'teachers/resetpassword.html'
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
		