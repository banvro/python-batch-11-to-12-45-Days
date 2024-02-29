from django.urls import path
from todos import views

urlpatterns = [
   path("", views.homepage, name="home"),
   path("alltodos", views.myalltodos, name="todos"),

   path("save-todo", views.savethinthistodo),

   path("done-todo/<int:id>", views.donetodo),
   path("delete-todo/<int:id>", views.deletetodo)
]
