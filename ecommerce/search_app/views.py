from django.shortcuts import render

# Create your views here.
from app1.models import product
from django.db.models import Q


def searchresult(request):
    prod=None
    query1=None
    if 'q' in request.GET:
        query1=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query1) | Q(desc__contains=query1))
    return render(request,'search.html',{'que1':query1,'produ':prod})