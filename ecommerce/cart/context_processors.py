from .models import  cart, cartitem
from . views import cart_id

def counter(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            cart1=cart.objects.filter(cart_id=cart_id(request))
            cart_item1=cartitem.objects.all().filter(cart=cart1[:1])
            for c_item in cart_item1:
                item_count += c_item.quantity
        except cart.DoesNotExist:
            item_count = 0
    return dict(item_c_key=item_count)

