from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration.forms import PersonForm
from registration.models import register, Branch


def loginfn(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user1=auth.authenticate(username=u,password=p)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('registration:loginfn')

    return render(request,'login.html')

def logfn(request,user):
    user=user
    return render(request, 'index.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def accepted(request):
    return render(request,'accepted.html')

class PersonCreateView(CreateView):
    model = register
    form_class = PersonForm
    template_name ='form.html '
    success_url = reverse_lazy('registration:accepted')

def load_cities(request):
    district_id = request.GET.get('country')
    cities = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'trial2.html', {'cities': cities})

def registerfn(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['psw']
        cp= request.POST['psw-repeat']

        if p == cp:
            if User.objects.filter(username=u):
                messages.info(request, 'username already taken')
                return redirect('registration:registerfn')
            else:
                user1 = User.objects.create_user(username=u, password=p)
                user1.save()
                print('user created')

        else:
            messages.info(request, 'password not match')
            return redirect('registration:registerfn')

        return redirect('registration:loginfn')

    return render(request,'register.html')