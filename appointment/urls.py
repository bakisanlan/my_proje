from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "appointment"

urlpatterns = [
    
    path("register/",views.register, name= "register"),
    path("login/",views.loginUser, name= "login"),
    path("logout/",views.logoutUser, name= "logout"),
    path("appointment_success/<int:id>",views.appointment_success, name= "appointment_success"),
    path("my_appointment/",views.my_appointment, name= "my_appointment"),
    path("delete_appointment/<int:id>",views.delete_appointment, name= "delete_appointment"),


    

]
