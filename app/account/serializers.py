from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'branch', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError("Passwords must match.")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
