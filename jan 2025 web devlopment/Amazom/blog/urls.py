from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("about", views.aboutus, name = "about"),
    path("contact", views.contactus, name = "contact"),
    path("services", views.servicesus, name = "services"),

    path("all-forms", views.allforms, name = "allforms"),

    path("save-data", views.savingdata, name = "savedata")
]