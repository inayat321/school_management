from django.conf.urls import url
from teachers.views import LoginView, DashboardView,LogoutView,PasswordView


app_name = 'teachers'
urlpatterns = [
	url(r'^reset/$', PasswordView.as_view(), name="passwordreset"),
	url(r'^logout/$', LogoutView.as_view(), name="logout"),
	url(r'^login/$',LoginView.as_view(),name="login_page"),
	url(r'^dashboard/$',DashboardView.as_view(), name="dashboard"),




]
