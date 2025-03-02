from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication



schema_view = get_schema_view(
    openapi.Info(
        title = "SAMJUNG ENC local system API",
        default_version="v1",
        description="This is a documentation for SAMJUNG ENC local system API",
        contact=openapi.Contact("dilshod.normurodov1392@gmail.com", "dil-shod.uz"),
    ),
    public=True,
    authentication_classes=[SessionAuthentication, BasicAuthentication, JWTAuthentication],
    permission_classes=[permissions.IsAuthenticated],
)


urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('admin/', include('user.boss.urls')),
    path('user/', include('user.urls')),
    path('document/', include('document.urls')),
    path('order/', include('order.urls')),
    path('chiller/', include('chiller.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('samjungdoc/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('samjungencredoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
