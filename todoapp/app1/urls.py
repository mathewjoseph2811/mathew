from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app1 import views
app_name='app1'
urlpatterns = [
    path('',views.fn1,name='fn1'),
    path('delete/<int:id>/',views.deletefn,name='deletefn'),
    path('update/<int:id>/',views.updatefn,name='updatefn'),
    path('list/',views.list.as_view(),name='list'),
    path('detail/<int:pk>/',views.detail.as_view(),name='detail'),
    path('update1/<int:pk>/',views.update.as_view(),name='update'),
    path('delete1/<int:pk>/',views.delete.as_view(),name='delete'),
]

if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)