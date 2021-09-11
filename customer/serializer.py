from rest_framework import serializers
from . models import Customer
from drivers.models import DriverCart

class CustomerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_current_province', 'customer_current_district', 'customer_finish_province', 'customer_finish_district', 'automobile', 'passengers_count', 'phone_number', 'date', 'latitude', 'longitude', 'sex']

class CustomerPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['status']

class CustomerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class DriverCartGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = ['id', 'driver', 'customer', 'amount', 'delivery_user', 'current_location', 'finish_location', 'empty_count']
