from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.homee, name = "home"), 
    path("about-us", views.aboutus, name = "about"),
    path("contact-us", views.contactus, name = "contact"),
    path("services", views.services, name = "services"),

    # my authanication pagess....
    path("login-page", views.loginn, name = "login"),
    path("sign-up", views.signuppage, name = "signup")
]
 