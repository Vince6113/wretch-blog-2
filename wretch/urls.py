from django.urls import path
from django.shortcuts import render
from django.contrib import admin


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")


urlpatterns = [path("about/", about), path("", home), path("admin/", admin.site.urls)]
