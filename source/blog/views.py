from django.shortcuts import render
from .models import Blog


def all_blog(request):
    obj = Blog.objects.order_by('-date')[:3]
    context = {
        "obj": obj,
    }
    return render(request, "blog_all.html", context)


def blog_detail(request, id):
    obj = Blog.objects.get(pk=id)
    context = {
        "obj": obj
    }
    return render(request, "blog_detail.html", context)
