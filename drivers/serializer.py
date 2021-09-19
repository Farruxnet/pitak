from rest_framework import serializers
from . models import Driver, DriverCart, Rating


# Haydovchi reytingi
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['user', 'rating_talk', 'rating_time', 'rating_clean']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['deriction', 'district', 'automobile', 'phone_number_one', 'phone_number_two', 'cooling_system', 'baggage', 'fuel', 'sex', 'status']
        extra_kwargs = {
            'district': {'validators': []}, # tumanlarni list ko'rinishida oladi
        }

class DriverGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
        extra_kwargs = {
            'district': {'validators': []}, # tumanlarni list ko'rinishida oladi
        }

# Haydovchi qidiruvga bergan elonlari
class DriverCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = ['empty_count', 'current_location', 'finish_location', 'delivery', 'rating', 'amount']

# Haydovchi qidiruvga bergan elonlarini oladi
class DriverCartGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = '__all__'

# Haydovchi qidiruvga bergan elonini o'zgartiradi
class DriverCartPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverCart
        fields = ['empty_count', 'current_location', 'finish_location', 'delivery', 'amount', 'status']















#
