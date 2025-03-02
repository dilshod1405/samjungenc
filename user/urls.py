from django.urls import path
from .views import LoginView, UserDetailsView, LogoutView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('me/<int:pk>/', UserDetailsView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
