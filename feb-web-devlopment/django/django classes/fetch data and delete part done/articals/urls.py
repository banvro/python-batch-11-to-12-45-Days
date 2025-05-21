from django.urls import path
from articals import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("about", views.aboutus, name = "about"),
    path("contact", views.contactus, name = "contact"),
    path("services", views.servicesus, name = "services"),
    
    path("saveing-data", views.saveinfo, name = "savee"),
    path("delete-data/<int:xyz>", views.deletedata, name = "deleting")
 
]