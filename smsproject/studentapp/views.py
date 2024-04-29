from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student


# Create your views here.
def studenthome(request):
    sid=request.session["sid"]
    return render(request,"studenthome.html",{"sid":sid})



def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["sid"] = sid  #creating a session
        return render(request,"studenthome.html",{"sid":sid})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("login failed ")

def studentchangepw(request):
    sid = request.session["sid"]
    return render(request,"studentchangepw.html",{"sid":sid})


def studentupdatepw(request):
    sid = request.session["sid"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid,opwd,npwd)

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=opwd))
    if flag:
        print("old pw is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated...")
        msg = "password updated"
    else:
        print("old pw is wrong")
        msg = "old password wrong"

    return render(request,"studentchangepw.html",{"sid":sid,"message":msg})


def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html",{"sid":sid})