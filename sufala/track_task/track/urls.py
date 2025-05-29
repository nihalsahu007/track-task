from django.urls import path
from .views import TaskAPIView, notification_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/tasks/', TaskAPIView.as_view()),
    path('api/tasks/<int:pk>/', TaskAPIView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('notifications/', notification_view, name='notifications'),
]
