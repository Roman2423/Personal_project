from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_list.as_view(), name="main_page"),
]