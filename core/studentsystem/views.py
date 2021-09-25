from typing import ContextManager
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from .models import AddStudents
from django.views.generic import UpdateView
from .forms import Edit
# Create your views here.

def home(request):
    all = AddStudents.objects.all()
    return render(request,"student/index.html",{
        "all":all
    })

def add(request):
    
    if request.method == "POST":
        sdtname= request.POST["sdtname"]
        sdtid= request.POST["sdtid"]
        sdtclass= request.POST["sdtclass"]
        sdttel= request.POST["sdttel"]
        sdtemail= request.POST["sdtemail"]
        sdtday= request.POST["sdtday"]
        parentname= request.POST["parentname"]

        addstudent = AddStudents(sdtname=sdtname, sdtid=sdtid,sdtclass=sdtclass, sdttel=sdttel, sdtemail=sdtemail, sdtday=sdtday,parentname=parentname )
        addstudent.save()
        return redirect("/student")
    return render(request, "student/add.html")


def detail(request,id):
    obj = AddStudents.objects.get(id=id)
    #obj = get_object_or_404(AddStudents,pk=id)
    return render(request,"student/detail.html",{
        "obj":obj
    })

def delete(request,id):
    if request.method == "POST":
        obj = get_object_or_404(AddStudents,id=id)
        obj.delete()
        return redirect("/student")
   


def edit(request,id):    
    if request.method == "POST":
        obj = AddStudents.objects.get(id=id)
        frm = Edit(request.POST,instance=obj)
        if frm.is_valid():
            frm.save()
            return redirect("/student")
    else:
        obj = AddStudents.objects.get(id=id)
        frm = Edit(instance=obj)
        
    return render(request,'student/edit.html',{"form":obj})
