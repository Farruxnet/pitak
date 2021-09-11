from rest_framework import serializers
from . models import Delivery

class DeliveryPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['delivery_current_location', 'delivery_current_district', 'delivery_finish_location', 'delivery_finish_district', 'delivery_type', 'latitude', 'longitude']

class DeliveryGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = '__all__'

class DeliveryPutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['found', 'status']






















#
