from rest_framework import serializers
from . models import SmsModel

class SmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmsModel
        fields = ['phone_number', 'code']
