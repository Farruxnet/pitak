from rest_framework import serializers
from . models import Customer
from drivers.models import DriverCart

# Mijoz haydovchi qidirish uchun kiritadigan ma'lumotlari
class CustomerPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['customer_current_province', 'customer_current_district', 'customer_finish_province', 'customer_finish_district', 'automobile', 'passengers_count', 'phone_number', 'date', 'latitude', 'longitude', 'sex']

# Mijoz haydovchi qidirish uchun kiritgan ma'lumotlarini o'zgartirish
class CustomerPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['status']

# Mijoz haydovchi qidirish uchun kiritgan ma'lumotlarini olish
class CustomerGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# Mijoz CustomerPostSerializer orqali kiritgan ma'lumotlarga mos haydovchilar ro'yxatini chiqaradi
class DriverCartGetAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = ['id', 'rating', 'driver', 'customer', 'amount', 'delivery_user', 'current_location', 'finish_location', 'empty_count']
