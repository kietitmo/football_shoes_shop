from django.urls import path
from .views import UserView, UserDetailView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', UserView.as_view() , name='get_or_create_users'),
    path('<uuid:id>', UserDetailView.as_view(), name='user-detail')
]
