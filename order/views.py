from order.models import Order
from order.serializers import OrderDetailsSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# get all orders
class OrdersView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderDetailsSerializer
    permission_classes = (IsAuthenticated,)