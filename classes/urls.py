from django.conf.urls import url
from classes.views import ClassListView
app_name = 'classes'
urlpatterns = [
	url('',ClassListView.as_view(),name="class_list"),

]