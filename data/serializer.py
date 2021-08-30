from rest_framework import serializers
from . models import Province, District, Deriction, Automobile

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class DerictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deriction
        fields = '__all__'

class AutomobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Automobile
        fields = '__all__'
















#
