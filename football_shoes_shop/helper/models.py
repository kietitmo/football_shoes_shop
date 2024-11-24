from rest_framework.response import Response

class ApiResponse:
    @staticmethod
    def success(data=None, message="Operation successful", http_code=200):
        response_data = {
            "message": message,
            "http_code": http_code,
            "data": data
        }
        return Response(response_data, status=http_code)

    @staticmethod
    def error(message="An error occurred", http_code=400):
        response_data = {
            "message": message,
            "http_code": http_code
        }
        return Response(response_data, status=http_code)
