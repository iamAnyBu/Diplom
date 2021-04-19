from django.conf.urls import url
from django.urls import path

from system import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
]