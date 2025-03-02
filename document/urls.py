from .views import DocumentsView, DocumentTypeView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'document_type', DocumentTypeView, basename='document_type')

urlpatterns = [
    path('', include(router.urls)),
    path('apps/', DocumentsView.as_view(), name='documents'),
]