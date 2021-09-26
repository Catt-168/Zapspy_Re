from django.shortcuts import render
from .models import Project


def hello(request):
    content = Project.objects.all()
    context = {
        "projects": content
    }
    return render(request, "hello.html", context)

