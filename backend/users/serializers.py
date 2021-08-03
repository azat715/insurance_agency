from rest_framework import fields, serializers

from users.models import Seller
from django.contrib.auth.models import User


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """в стандартный токен добавляю user.id
    """
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        # and everything else you want to send in the response
        return data



class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seller
        fields = ["username", "email", "password"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

