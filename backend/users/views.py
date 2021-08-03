
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from users.serializers import CustomTokenObtainPairSerializer, SellerSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.models import Seller

@permission_classes([IsAuthenticated])
class SellerRetrieveAPIView(RetrieveAPIView):
    """GET Seller info
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


@permission_classes([AllowAny])
class SellerCreateAPIView(CreateAPIView):
    """GET Seller info
    POST - create seller
    """
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer



class CustomTokenObtainPairView(TokenObtainPairView):
    """Token с user.id
    """
    serializer_class = CustomTokenObtainPairSerializer