from django.shortcuts import render

# Create your views here.
def homefn(request):
    return render(request,'index.html')

