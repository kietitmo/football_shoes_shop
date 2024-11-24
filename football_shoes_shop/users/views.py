from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from helper.models import ApiResponse
from .serializers import UserSerializer
from .models import User
from .permissions import IsOwner
from .filters import UserFilter

class UserPagination(PageNumberPagination):
    page_size = 3  # Số lượng user trên mỗi trang
    page_size_query_param = 'page_size'
    max_page_size = 100

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    # Lấy tất cả users
    def get(self, request):
        if not request.user.is_staff:  # Chỉ superuser mới được phép
            return ApiResponse.error("You do not have permission to view all users.", status.HTTP_403_FORBIDDEN)

        # Lấy các query params từ request để lọc
        filter_set = UserFilter(request.query_params, queryset=User.objects.all())
        
        # Kiểm tra nếu filter hợp lệ và áp dụng phân trang
        if filter_set.is_valid():
            users = filter_set.qs  
            paginator = UserPagination()
            paginated_users = paginator.paginate_queryset(users, request) 
            
            serializer = UserSerializer(paginated_users, many=True)

            return ApiResponse.success({
                'total_items': paginator.page.paginator.count,  
                'items_in_this_page': len(paginated_users),
                'next': paginator.get_next_link(),  
                'previous': paginator.get_previous_link(),  
                'results': serializer.data 
            }, message="Get all users successfully", http_code=200)
        else:
            return ApiResponse.error(filter_set.errors, http_code=400)

    # Tạo mới một user
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_serializer = UserSerializer(user)
            return ApiResponse.success(user_serializer.data, "User created successfully", status.HTTP_201_CREATED)
        return ApiResponse.error(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
class UserDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    # Lấy thông tin một user theo ID
    def get(self, request, id):
        user = get_object_or_404(User, pk=id)

        # Kiểm tra quyền sở hữu
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return ApiResponse.success(serializer.data, "Get user successfully", status.HTTP_200_OK)
    
    #  Cập nhật thông tin user
    def put(self, request, id):
        user = get_object_or_404(User, id=id)

        # Kiểm tra quyền sở hữu
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, data=request.data, partial=True)  # partial=True để cập nhật từng phần
        if serializer.is_valid():
            user = serializer.save()
            return ApiResponse.success(UserSerializer(user).data, "User updated successfully", status.HTTP_200_OK)
        return ApiResponse.error(serializer.errors, status.HTTP_400_BAD_REQUEST)

    # Xóa một user
    def delete(self, request, id):
        user = get_object_or_404(User, id=id)

        # Kiểm tra quyền sở hữu
        self.check_object_permissions(request, user)

        user.delete()
        return ApiResponse.success(None, "User deleted successfully", status.HTTP_204_NO_CONTENT)
