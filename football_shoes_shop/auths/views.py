from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from auths.models import EmailVerificationToken
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from helper.models import ApiResponse
from .serializers import UserRegistrationSerializer


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]  # Chấp nhận yêu cầu từ bất kỳ ai

    def post(self, request):
        # Dữ liệu từ yêu cầu
        serializer = UserRegistrationSerializer(data=request.data)

        # Kiểm tra tính hợp lệ của dữ liệu
        if serializer.is_valid():
            # Tạo người dùng mới
            user = serializer.save()

            token = EmailVerificationToken.objects.create(user=user)

            # Tạo nội dung HTML từ template
            verification_url = f"{settings.FRONTEND_URL}/auths/verify-email/{token.token}/"
            html_content = render_to_string('email_verification.html', {
                'email': user.email,
                'verification_url': verification_url,
            })

            # Gửi email xác thực
            subject = "Xác thực tài khoản Shoes Shop"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [user.email]
            email = EmailMultiAlternatives(subject, body="Please verify your email.", from_email=from_email, to=recipient_list)
            email.attach_alternative(html_content, "text/html")  # Thêm HTML nội dung email
            email.send()

            # Gửi phản hồi thành công
            return ApiResponse.success({"id": user.id, "email": user.email}, message="User created successfully", http_code=status.HTTP_201_CREATED)

        # Trả về lỗi nếu dữ liệu không hợp lệ
        return ApiResponse.error(serializer.errors, http_code=status.HTTP_400_BAD_REQUEST)

class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            verification_token = EmailVerificationToken.objects.get(token=token)
            if not verification_token.is_valid():
                return ApiResponse.error("Token is invalid", status.HTTP_400_BAD_REQUEST)

            # Kích hoạt tài khoản
            user = verification_token.user
            user.is_active = True
            user.save()

            # Xóa token sau khi sử dụng
            verification_token.delete()

            return ApiResponse.success({"id": user.id, "email": user.email},"Email verified successful.", status.HTTP_200_OK)
        except EmailVerificationToken.DoesNotExist:
            return ApiResponse.error("Token is invalid", status.HTTP_400_BAD_REQUEST)