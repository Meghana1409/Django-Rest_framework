from django.urls import path,include
from customerorder import views

urlpatterns=[
    path('customer/',views.CustomerList.as_view()),
    path('customer/<int:pk>',views.CustomerDetails.as_view()),
    path('order/',views.OrderList.as_view()),
    path('order/<int:pk>',views.OrderDetails.as_view()),
]