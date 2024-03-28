# registration/serializers.py
from rest_framework import serializers
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'branch', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            branch=validated_data['branch'],
            username=validated_data['email'],  # Using email as username
            password=validated_data['password']
        )
        return user
