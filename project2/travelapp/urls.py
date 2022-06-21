from django.urls import path

from travelapp import views

urlpatterns=[
    path('',views.fn1,name='fn1'),
    path('register',views.register1,name='register1')
]