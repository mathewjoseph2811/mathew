import os
from unittest import result

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files import File

# Create your views here.
from app1.forms import movieform
from app1.models import table1


def fn1(request):
    v1=table1.objects.all()
    context={
        'k1':v1
    }
    return render(request,'h1.html',context)

def fn2(request,table1_id):
   v1=table1.objects.get(id=table1_id)
   return render(request,'details.html',{'k':v1})

def addfn(request):
    if request.method =="POST":
        name=request.POST.get('name')
        desc=request.POST.get('desc')
        details=request.POST.get('details')
        img1=request.FILES['imag']
        var1=table1(name=name,desc=desc,details=details,img=img1,)
        var1.save()
    return render(request,'add1.html')

def update(request,id):
    v1=table1.objects.get(id=id)
    v2=movieform(request.POST or None, request.FILES,instance=v1)
    if v2.is_valid():
        v2.save()
        return redirect('/')
    return render(request,'edit.html',{'k1':v2,'k2':v1})

def delete(request,id):
    if request.method=='POST':
      m1=table1.objects.get(id=id)
      m1.delete()
      return redirect('/')
    return render(request,'delete.html')