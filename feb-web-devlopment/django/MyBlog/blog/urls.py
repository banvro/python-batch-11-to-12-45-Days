from django.urls import path
from blog import views

urlpatterns = [
    path("", views.hommepage, name = "home"),
    path("about", views.aboutus, name="about"),
]
