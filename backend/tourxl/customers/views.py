from rest_framework.viewsets import ModelViewSet

from customers.models import Customers
from customers.serializers import CustomersSerializer


class CustomersViewSet(ModelViewSet):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
