import django_filters
from .models import User

class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(lookup_expr='icontains', label="Username")
    email = django_filters.CharFilter(lookup_expr='icontains', label="Email")
    first_name = django_filters.CharFilter(lookup_expr='icontains', label="First Name")
    last_name = django_filters.CharFilter(lookup_expr='icontains', label="Last Name")
    address = django_filters.CharFilter(lookup_expr='icontains', label="Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'address']
