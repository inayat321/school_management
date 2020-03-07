from django import template
from django.utils.html import format_html
from classes.models import Classes
from students.models import Students

register = template.Library()


@register.simple_tag
def class_list():
	str1 = ""
	for clas in Classes.objects.all():
		str1 += "<li>"+ "<a class='drpa' href=/students/"+str(clas.id)+"/>"+ clas.name +"</a>" +"</li>" 
	return format_html(str1)

