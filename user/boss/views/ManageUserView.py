from user.serializers import UserSerializer, LoginSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from user.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create, Update, Delete user by admin
class ManageUserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

