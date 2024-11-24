from rest_framework import serializers
from users.models import User
from django.contrib.auth.password_validation import validate_password

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirmation', 'phoneNumber', 'address', 'avatar']

    def validate(self, attrs):
        # Kiểm tra xem mật khẩu và xác nhận mật khẩu có khớp không
        if attrs['password'] != attrs['password_confirmation']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        # Tạo người dùng mới
        validated_data.pop('password_confirmation')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = User.objects.create_user(email=email, password=password, is_active=False, **validated_data)
        return user
