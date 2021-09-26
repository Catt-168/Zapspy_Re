from django.shortcuts import render
import random


def home(request):
    return render(request, "home.html")


def password(request):
    large_char = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    numbers = list("1234567890")
    special_char = list("!@#$%^&*")
    _password = list("abcdefghijklmnopqrstuvwxyz")
    length = int(request.GET.get("length"))
    if request.GET.get("u_case"):
        _password.extend(large_char)
    if request.GET.get("number"):
        _password.extend(numbers)
    if request.GET.get("special"):
        _password.extend(special_char)
    print(_password)
    f_pass = ""
    for i in range(length):
        f_pass += random.choice(_password)
    context = {
        "password": f_pass
    }
    return render(request, "password.html", context)