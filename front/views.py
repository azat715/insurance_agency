from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import Product

from .serializers import ProductSerializer

# Create your views here.
@api_view()
def products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


def main(request):
    return render(request, "home.html")
