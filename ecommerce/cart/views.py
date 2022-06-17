from django.shortcuts import render, redirect, get_object_or_404
from app1.models import product
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
from cart.models import cart,cartitem


def cart_id(request):
    cart1=request.session.session_key
    if not cart1:
        cart1=request.session.create()
    return cart1

def add_cart(request,product_id):
    product1=product.objects.get(id=product_id)

    try:
        cart1=cart.objects.get(cart_id=cart_id(request))
    except cart1.DoesNotExist:
        cart1=cart.objects.create(cart_id=cart_id(request))
        cart1.save()
    try:
        cartitem1=cartitem.objects.get(product=product1,cart=cart1)
        if cartitem1.quantity < cartitem1.product.stock:
            cartitem1.quantity += 1
        cartitem1.save()
    except cartitem.DoesNotExist:
        cartitem1=cartitem.objects.create(product=product1,quantity=1,cart=cart1)
        cartitem1.save()
    return redirect('cart:cart_detail')

def cart_detail(request,total=0,counter=0,cart_items=None):
    try:
        cart3=cart.objects.get(cart_id=cart_id(request))
        cart_items=cartitem.objects.filter(cart=cart3,active=True)
        for cart_i in cart_items:
            total += (cart_i.product.price * cart_i.quantity)
            counter += cart_i.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items_key=cart_items,total_key=total,counter_key=counter))

def cart_remove(request,product_id):
    cart1=cart.objects.get(cart_id=cart_id(request))
    prod1=get_object_or_404(product,id=product_id)
    cart_item1=cartitem.objects.get(product=prod1,cart=cart1)
    if cart_item1.quantity > 1:
        cart_item1.quantity -= 1
        cart_item1.save()
    else:
        cart_item1.delete()
    return redirect('cart:cart_detail')

def cart_item_delete(request,product_id):
    cart1=cart.objects.get(cart_id=cart_id(request))
    prod1=get_object_or_404(product,id=product_id)
    cart_item1=cartitem.objects.get(product=prod1,cart=cart1)
    cart_item1.delete()
    return redirect('cart:cart_detail')
