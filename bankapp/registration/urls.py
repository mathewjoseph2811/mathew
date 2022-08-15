from . import views
from django.urls import path, include
app_name='registration'

urlpatterns = [
    path('',views.registerfn,name='registerfn'),
    path('login/',views.loginfn,name='loginfn'),
    path('logedpage/',views.logfn,name='logfn'),
    path('logout/',views.logout,name='logout'),
    path('accepted/', views.accepted, name='accepted'),
    path('add/', views.PersonCreateView.as_view(), name='person_add'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),
]