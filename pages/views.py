from django.shortcuts import render


def home(request):
    lottery_number = [1, 2, 4, 5, 11]
    return render(request, "pages/home.html", {"lucky": lottery_number})


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    return render(request, "pages/contact.html")
