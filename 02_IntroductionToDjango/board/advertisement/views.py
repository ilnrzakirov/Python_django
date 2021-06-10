from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

def advertisement_list (request, *args, **kwargs):
    return render(request, "advertisement/advertisement_list.html", {})

def home_work_python (request, *args, **kwargs):
    return render(request, "advertisement/home_work_python.html", {})

def home_work_java(request, *args, **kwargs):
    return render(request, "advertisement/home_work_java.html", {})

def home_work_php(request, *args, **kwargs):
    return render(request, "advertisement/home_work_php.html", {})

def home_work_c(request, *args, **kwargs):
    return render(request, "advertisement/home_work_c.html", {})

def home_work_js(request, *args, **kwargs):
    return render(request, "advertisement/home_work_js.html", {})

def CourseC(request, *args, **kwargs):
    return redirect("https://skillbox.ru/course/profession-c-plus-plus/")

def CourseJava(request, *args, **kwargs):
    return redirect("https://skillbox.ru/course/profession-java/")

def CourseJS(request, *args, **kwargs):
    return redirect("https://skillbox.ru/course/profession-fullstack-js/")

def CoursePHP(request, *args, **kwargs):
    return redirect("https://skillbox.ru/course/profession-fullstack-php/")

def CoursePython(request, *args, **kwargs):
    return redirect("https://skillbox.ru/course/profession-python/")


