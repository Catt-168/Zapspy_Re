from django.urls import path
from .views import hello

app_name = "port"
urlpatterns = [
    path("", hello, name="hello-view")
]
