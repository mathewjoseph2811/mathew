
from django.urls import path, include

from . import views
app_name='app1'
urlpatterns = [
    path('',views.fn1,name='fn1'),
    path('test/<int:table1_id>/',views.fn2,name='fn2'),
    path('add/',views.addfn,name='addfn'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
]