from django.urls import path, include
from. import views

urlpatterns = [
    path("checkstudentlogin", views.checkstudentlogin, name="checkstudentlogin"),
    path("studenthome", views.studenthome, name="studenthome"),
    path("studentchangepw", views.studentchangepw, name="studentchangepw"),
    path("studentupdatepw", views.studentupdatepw, name="studentupdatepw"),
    path("studentcourses", views.studentcourses, name="studentcourses"),

]