from django.urls import path
from django.shortcuts import render


def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")


urlpatterns = [
    path("about/", about),
    path("", home),
]
