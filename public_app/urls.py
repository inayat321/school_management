from django.conf.urls import url
from public_app.views import HomeView


urlpatterns = [
    url('', HomeView.as_view()),
]