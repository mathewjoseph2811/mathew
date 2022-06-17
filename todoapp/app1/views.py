from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from .forms import updateform
from app1.models import task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView

def fn1(request):
    var=task.objects.all()
    if request.method=='POST':
        n1=request.POST.get('n')
        p1=request.POST.get('pri')
        d=request.POST.get('date')
        v1=task(name=n1,priority=p1,date=d)
        v1.save()
    return render(request,'home.html',{'k1':var})

def deletefn(request,id):
    if request.method=='POST':
        ta=task.objects.get(id=id)
        ta.delete()
        return redirect('/')
    return render(request,'delete.html')

def updatefn(request,id):
    up=task.objects.get(id=id)
    upform=updateform(request.POST or None,request.FILES,instance=up)
    if upform.is_valid():
        upform.save()
        return redirect('/')
    return render(request,'update.html',{'u':up,'uf':upform})

class list(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'k1'

class detail(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'd'

class update(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')


    def get_success_url(self):
        return reverse_lazy('app1:detail',kwargs={'pk':self.object.id})

class delete(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('app1:fn1')