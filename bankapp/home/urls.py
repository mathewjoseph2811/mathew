from django.conf.urls.static import static

from . import views
from django.urls import path, include
app_name='home'

urlpatterns = [
    path('',views.homefn,name='homefn'),
]

