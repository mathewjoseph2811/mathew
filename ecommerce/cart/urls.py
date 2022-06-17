from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from cart import views
app_name='cart'

urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/', views.cart_item_delete, name='cart_item_delete'),

    ]