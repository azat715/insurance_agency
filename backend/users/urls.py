from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views import SellerRetrieveAPIView, SellerCreateAPIView, CustomTokenObtainPairView

app_name = "users"

urlpatterns = [
    path("<int:pk>/", SellerRetrieveAPIView.as_view(), name="user_info"),
    path("", SellerCreateAPIView.as_view(), name="user_create"),
    path("token/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
