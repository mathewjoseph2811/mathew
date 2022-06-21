from django.contrib.auth.models import User
from django.shortcuts import render
from .models import travel,person
# Create your views here.

def fn1(request):
    obj=travel.objects.all()
    obj1=person.objects.all()
    return render(request,'index.html',{'key':obj,'key1':obj1})

def register1(request):
  if request.method== 'POST':
    u=request.POST['username']
    p=request.POST['password']
    cp=request.POST['cpassword']
    e=request.POST['email']
    fn=request.POST['first_name']
    ln=request.POST['last_name']

    user1=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
    user1.save()
    print('user created')

  return render(request,'registration.html')