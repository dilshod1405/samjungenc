from document.serializers import DocTypeSerializer, DocAppSerializer
from rest_framework import generics, viewsets
from document.models import DocType, DocApp
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# get all documents
class DocumentsView(generics.ListCreateAPIView):
    queryset = DocApp.objects.all()
    serializer_class = DocAppSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# CRUD Document Type
class DocumentTypeView(viewsets.ModelViewSet):
    queryset = DocType.objects.all()
    serializer_class = DocTypeSerializer
    permission_classes = (IsAdminUser,)