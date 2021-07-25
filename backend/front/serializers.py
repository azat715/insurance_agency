from rest_framework import fields, serializers

from core.models import Product, Customer


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "active",
            "description",
            "id",
            "insurance_period",
            "name",
            "percentage_rate",
            "price",
            "published",
            "type",
            "seller",
        ]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        customer = Customer(
            name=validated_data["name"],
            telephone=validated_data["telephone"],
            email=validated_data["email"],
            product=validated_data["product"],
        )
        customer.save()
        return customer
