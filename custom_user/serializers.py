from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    # passwords should not be sent during response
    # deserialization flow serializer flow is field to internal value field level object level and the create method.
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone_number',
            'role',
            'profile_photo'
        ]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    
    def to_internal_value(self, data):
        data = data.copy()
        if data.get('phone_number'):
            phone_number = "+977-" + data.get('phone_number')
            data['phone_number'] = phone_number
        return super().to_internal_value(data)
    
    
    def validate_phone_number(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("phone number cannot be less than 10")
        return value

    
