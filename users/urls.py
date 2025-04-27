from django.urls import path

from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, TokenBlacklistView)

from users import views


# urls

urlpatterns = [
    path("profile/", views.UserRetrieveAPIView.as_view(), name="user-profile"),
    path("users/signup/", views.UserCreateAPIView.as_view(), name="user-signup"),

    path("users/token/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("users/token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("users/token/blacklist/", TokenBlacklistView.as_view(), name="token-blacklist"),
]