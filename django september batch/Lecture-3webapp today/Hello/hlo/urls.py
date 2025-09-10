from django.urls import path
from hlo import views

urlpatterns = [
    path("home", views.homepage, name = "home"),
    path("about", views.aboutus, name = "about"),
    path("contact", views.contactus, name = "contact")
]