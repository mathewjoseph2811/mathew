from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login1(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user1=auth.authenticate(username=u,password=p)
        if user1 is not None:
          auth.login(request,user1)
          return redirect('/')
        else:
          messages.info(request,'invalid credentials')
          return redirect('login1')


    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')

def register1(request):
  if request.method== 'POST':
    u=request.POST['username']
    p=request.POST['password']
    cp=request.POST['cpassword']
    e=request.POST['email']
    fn=request.POST['first_name']
    ln=request.POST['last_name']

    if p==cp:
     if User.objects.filter(username=u):
       messages.info(request,'username already taken')
       return redirect('register1')
     if User.objects.filter(email=e):
       messages.info(request,'email already registered')
       return redirect('register1')
     else:
       user1=User.objects.create_user(username=u,password=p,email=e,first_name=fn,last_name=ln)
       user1.save()
       print('user created')

    else:
     messages.info(request,'password not match')
     return redirect('register1')

    return redirect('login1')

  return render(request,'registration.html')