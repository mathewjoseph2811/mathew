from django.contrib import admin

# Register your models here.
from .models import cart,cartitem

admin.site.register(cart),
admin.site.register(cartitem)