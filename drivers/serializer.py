from rest_framework import serializers
from . models import Driver, DriverCart

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class DriverCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = '__all__'















#
