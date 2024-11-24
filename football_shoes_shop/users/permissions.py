from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Chỉ cho phép người dùng truy cập hoặc chỉnh sửa thông tin của chính họ.
    """
    def has_object_permission(self, request, view, obj):
        # Kiểm tra nếu `obj` là người dùng hiện tại
        if request.user.is_superuser:
            return True
        return obj == request.user

class IsSuperUser(BasePermission):
    """
    Chỉ cho phép người dùng truy cập hoặc chỉnh sửa thông tin của chính họ.
    """
    def has_permission(self, request, view):
        # Kiểm tra nếu `obj` là người dùng hiện tại
        return request.user and request.user.is_superuser
