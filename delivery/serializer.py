from rest_framework import serializers
from . models import Delivery

# Mijoz pochta qo'shish
class DeliveryPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['delivery_current_location', 'delivery_current_district', 'delivery_finish_location', 'delivery_finish_district', 'delivery_type', 'latitude', 'longitude']

# Mijoz qo'shgan pochtasini ko'rish olish
class DeliveryGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'

# Mijoz e'lonini o'zgartirish
class DeliveryPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['found', 'status']






















#
