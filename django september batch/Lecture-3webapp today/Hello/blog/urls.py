from django.urls import path
from blog import views


urlpatterns = [
    path("blog-1", views.bloging1, name = "blog1"),
    path("blog-2", views.bloging2, name = "blog2"),
]