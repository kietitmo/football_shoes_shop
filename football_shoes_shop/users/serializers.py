from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    def validate_email(self, value):
        if "@" not in value:
            raise serializers.ValidationError("Invalid email address")
        return value

    def validate_password(self, value):
        if value.isalnum():
            raise serializers.ValidationError('Password must have at least one special character.')
        return value
    
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'phoneNumber', 'address', 'avatar']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # Mã hóa mật khẩu
        user.save()
        return user

