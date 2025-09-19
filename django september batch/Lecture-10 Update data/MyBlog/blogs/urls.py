from django.urls import path
from blogs import views

urlpatterns = [
    path("", views.homee, name = "home"), 
    path("about-us", views.aboutus, name = "about"),
    path("contact-us", views.contactus, name = "contact"),
    path("services", views.services, name = "services"),

    # my authanication pagess....
    path("login-page", views.loginn, name = "login"),
    path("sign-up", views.signuppage, name = "signup"),

    # svaing contact us form
    path("save-form-data", views.savinginfo, name = "saving"),

    # for adding employe from
    path("add-employee", views.adding_employee, name = "addingemp"),

    # showing data
    path("all-contact-us-forms", views.allcontactus, name = "allforms"),
    path("all-employee", views.allemployee, name = "allemp"),

    # deleteing records
    path("delete-employe/<int:x>", views.deletingemp, name = "deleteemp"),
    path("delete-contact-from/<int:xyz>", views.contactdelete, name = "contact"),

    # updating data..
    path("emp-record/<int:update_id>", views.updateemp, name = "empupdate"),
    path("emp-update/<int:update_id>", views.empupdate, name = "emp"),

    path("contact-update/<int:contact_id>", views.updatecontactform, name = "updatecontact")
]
 