from django.urls import path, include
# from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('coffeeholic/', views.CoffeeShopList.as_view(), name='coffeeshop_list'),
    path('coffeeholic/<int:pk>', views.CoffeeShopDetail.as_view(),
         name='coffeeshop_detail'),
]
