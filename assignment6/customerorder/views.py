from django.shortcuts import render
from .serializer import OrderSerializer,CustomerSerializer
from .models import Customer,Order
from rest_framework import generics

# Create your views here.
class CustomerList(generics.ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class CustomerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class OrderList(generics.ListCreateAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer
