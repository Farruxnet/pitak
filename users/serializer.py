from rest_framework import serializers
from . models import User
import hashlib

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'name', 'password', 'language', 'device', 'profile_photo']

    def create(self, validate_data):
        user = User.objects.create(phone_number=validate_data['phone_number'], language = validate_data['language'], device=validate_data['device'])
        user.set_password(hashlib.md5(f'{validate_data["password"]}'.encode("utf-8")).hexdigest()[:10])
        user.save()
        print(validate_data)
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'status', 'profile_photo', 'language', 'device', 'description', 'account', 'create_at']


class UserUpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'phone_number', 'profile_photo', 'status', 'language', 'device', 'description']
