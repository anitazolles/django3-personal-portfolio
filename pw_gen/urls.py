from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_pwd,name='home_pwd'), ## '' is our homepage
    path('password/',views.password,name='password'),
]
