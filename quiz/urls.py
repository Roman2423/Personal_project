from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.quiz_list, name="main_page"),
    path('quiz-creation/', views.quiz_create, name="quiz_creation")
]