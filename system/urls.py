from django.conf.urls import url
from system import views

urlpatterns = [
    url(r'^', views.base, name='base'),
]