from django.contrib import admin
from django.urls import path

from wer import views

urlpatterns = [
    path('admin/', admin.site.urls),

   # path('asd/', views.asd),
   # path('das/', views.das),
   # path('reverse/', views.reverse, name = 'reverse'),
   # path('', views.koko),
    path('', views.index),
    path('registration/', views.reg),
    path('login/', views.login),
]
