from rest_framework import serializers

from apps.kiosko.models import *



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models= Product
        fields = '__all__'