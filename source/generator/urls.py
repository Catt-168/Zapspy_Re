from django.urls import path
from .views import home, password


urlpatterns = [
    path("", home, name="home-view"),
    path("password/", password, name="password"),
]
