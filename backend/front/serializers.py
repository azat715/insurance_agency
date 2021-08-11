from rest_framework import serializers

from core.models import Product


class ProductSerializer(serializers.ModelSerializer):
    url_buy = serializers.CharField(source="buy_url", read_only=True)
    url_detail = serializers.CharField(source="detail_url", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
