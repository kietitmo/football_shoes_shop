from math import floor
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status
from helper.models import ApiResponse

class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Gọi phương thức authenticate mặc định
        validated_token = super().authenticate(request)
        if validated_token:
            user = validated_token[0]
            token = validated_token[1]
            # Kiểm tra iat so với last_login
            iat = token.get('iat', None)
            if iat and user.last_login:
                    if int(iat) < floor(user.last_login.timestamp()):
                        # return ApiResponse.error("Token is invalid due to a newer login", 401)
                        raise AuthenticationFailed("Token is invalid due to a newer login")
            
            return user, token
        return None
