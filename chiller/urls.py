from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChillerView, ChillerImageView

router = DefaultRouter()
router.register(r'chiller', ChillerView, basename='chiller')
router.register(r'chiller_image', ChillerImageView, basename='chiller_image')

urlpatterns = [
    path('', include(router.urls)),
]