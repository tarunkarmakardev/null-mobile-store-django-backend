from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import SignUpView, UserInfoView


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user_info/', UserInfoView.as_view(), name='user_info'),
]
