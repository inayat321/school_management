from django.contrib import admin
from teachers.models import TeacherClasses

# Register your models here.


class TeacherClassesAdmin(admin.ModelAdmin):
	list_display = ('teacher', 'teacher_class')

admin.site.register(TeacherClasses, TeacherClassesAdmin)
