
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer
from apps.kiosko.models import *
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

