from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views.ManageUserView import ManageUserView

router = DefaultRouter()
router.register(r'users', ManageUserView, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]