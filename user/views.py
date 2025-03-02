from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveAPIView
from user.models import User
from user.serializers import LoginSerializer

# Login
class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get user details
class UserDetailsView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated,)


# Logout
class LogoutView(APIView):
    def post(self, request):
        user = request.user
        user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)