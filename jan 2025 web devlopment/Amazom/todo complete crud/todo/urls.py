from django.urls import path
from todo import views

urlpatterns = [
    path("", views.homepage, name = "home"),
    path("contect", views.contact, name = "contact"),
    path("saving", views.saving),

    path("deletedata/<int:id>", views.deletethis),

    path("updatedata/<int:myid>", views.updating),

    path("updatenow/<int:myid>", views.updatingnow),
]
