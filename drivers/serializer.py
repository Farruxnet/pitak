from rest_framework import serializers
from . models import Driver, DriverCart

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['deriction', 'district', 'automobile', 'phone_number_one', 'phone_number_two', 'cooling_system', 'baggage', 'fuel', 'sex', 'status']
        extra_kwargs = {
            'district': {'validators': []}, # remove uniqueness validation
        }

class DriverGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
        extra_kwargs = {
            'district': {'validators': []}, # remove uniqueness validation
        }

class DriverCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = ['empty_count', 'current_location', 'finish_location', 'delivery']

class DriverCartGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = '__all__'















#
