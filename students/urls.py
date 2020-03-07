from django.conf.urls import url
from students.views import StudentListView

app_name = 'students'
urlpatterns = [
	url(r'^(?P<pk>[0-9]+)/$',StudentListView.as_view(),name="student_list"),





]