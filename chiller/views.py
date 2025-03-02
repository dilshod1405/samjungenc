from .serializers import ChillerSerializer, ChillerImageSerializer
from rest_framework import viewsets
from .models import Chiller, ChillerImage
from rest_framework.permissions import IsAuthenticated


class ChillerView(viewsets.ModelViewSet):
    queryset = Chiller.objects.all()
    serializer_class = ChillerSerializer
    permission_classes = (IsAuthenticated,)


class ChillerImageView(viewsets.ModelViewSet):
    queryset = ChillerImage.objects.all()
    serializer_class = ChillerImageSerializer
    permission_classes = (IsAuthenticated,)