from django.shortcuts import render


def home(request):
    return render(request, "tasks/first_page.html")


def login(request):
    return render(request, "tasks/login_registration.html")
