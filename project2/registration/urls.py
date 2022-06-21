from django.urls import path

from registration import views

urlpatterns=[
    path('register',views.register1,name='register1'),
    path('login',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
]