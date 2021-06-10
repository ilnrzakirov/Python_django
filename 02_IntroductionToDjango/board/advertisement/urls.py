from django.urls import path
from .import views


urlpatterns = [
    path('', views.advertisement_list, name="advertisement_list"),
    path('home_work_python', views.home_work_python, name="python"),
    path('home_work_java', views.home_work_java, name="java"),
    path('home_work_php', views.home_work_php, name="php"),
    path('home_work_c', views.home_work_c, name="c"),
    path('home_work_js', views.home_work_js, name="js"),
    path('CourseC', views.CourseC, name="CourseC"),
    path('CourseJava', views.CourseJava, name="CourseJava"),
    path('CourseJS', views.CourseJS, name="CourseJS"),
    path('CoursePHP', views.CoursePHP, name="CoursePHP"),
    path('CoursePython', views.CoursePython, name="CoursePython"),
]