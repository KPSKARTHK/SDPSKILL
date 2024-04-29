from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

def demofunction(request):
    return HttpResponse("<h3 align=center >PFSD SDP Project")
def demofunction1(request):
    return HttpResponse("KL UNIVERSITY")
def demofunction2(request):
    return HttpResponse("Student Management System")
def homefunction(request):
    return render(request,"index.html")
def aboutfunction(request):
    return render(request,"about.html")
def loginfunction(request):
    return render(request,"logins.html")
def facultylogin(request):
    return render(request,"facultylogin.html")
def studentlogin(request):
    return render(request,"studentlogin.html")
def contactfunction(request):
    return render(request,"contact.html")
