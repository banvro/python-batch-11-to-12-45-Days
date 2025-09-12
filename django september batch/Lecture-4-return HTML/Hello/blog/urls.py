from django.urls import path
from blog import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("about", views.aboutus, name = "about"),
    path("login-page", views.loginpage, name = "login"),
    path("singn-up", views.signuppage, name = "signup")
]