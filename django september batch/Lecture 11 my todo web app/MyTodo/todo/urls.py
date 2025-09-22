from django.urls import path
from todo import views

urlpatterns = [
    path("", views.todohome, name = "todo"),
    path("save-todo", views.savingtodo, name = "svetodo"),
    
    # deleteig todo
    path("delete-todo/<int:x>", views.deletetodo, name = "deletetodo"),

    #upudate data
    path("update-todo/<int:xyz>", views.todoupdate, name = "updatetodo")
]
