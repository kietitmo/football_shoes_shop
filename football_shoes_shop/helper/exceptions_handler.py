from rest_framework.views import exception_handler
from helper.models import ApiResponse

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Kiểm tra nếu có lỗi từ DRF
    if response is not None:
        # Trả về lỗi với ApiResponse format
        return ApiResponse.error(message=str(exc), http_code=response.status_code)
    
    # Nếu không có lỗi từ DRF, trả về lỗi mặc định
    return ApiResponse.error(message="An unknown error occurred", http_code=500)