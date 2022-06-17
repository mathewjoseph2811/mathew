from gc import get_objects

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator,InvalidPage,EmptyPage

# Create your views here.
from .models import category, product


def allProdCat(request,c_slug=None):
    c_page=None
    products=None

    if c_slug != None:
        c_page=get_object_or_404(category,slug=c_slug)
        products=product.objects.all().filter(category=c_page,available=True)
    else:
        products=product.objects.all().filter(available=True)


    paginator1=Paginator(products,6)
    try:
        page1=int(request.GET.get('page','1'))
    except:
        page1=1
    try:
        prod1=paginator1.page(page1)
    except (EmptyPage,InvalidPage):
        prod1=paginator1.page(paginator1.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products,'pro':prod1})

def proDetail(request,c_slug,p_slug):
    try:
        prod=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'pro_key':prod,})