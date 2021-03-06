from django.urls import path

from system import views

# АДРЕСА ПЕРЕХОДОВ К ФУНКЦИЯМ ВО views.py
urlpatterns = [
    path('', views.base, name='base'),
    path('base_login/',views.base_login, name='base_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('whoau/', views.whoau, name='whoau'),
    path('shef/', views.shef, name='shef'),
    path('empl/', views.empl, name='empl'),
    path('anketa/', views.anketa, name='anketa'),
    path('test/', views.test, name='test'),
    path('plan/', views.plan, name='plan'),
]
