from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def visitor_login(request):
    return render(request, "login.html")
