from rest_framework import serializers
from . models import User
import hashlib

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'password', 'language', 'device']

    def create(self, validate_data):
        user = User.objects.create(phone_number=validate_data['phone_number'])
        user.set_password(hashlib.md5(f'{validate_data["password"]}'.encode("utf-8")).hexdigest()[:10])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'profile_photo', 'language', 'device', 'account', 'create_at']
