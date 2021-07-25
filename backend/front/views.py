from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins

from core.models import Product, Customer

from .serializers import ProductSerializer, CustomerSerializer


class ProductsList(generics.ListCreateAPIView, generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        """ """
        queryset = Product.objects.all()
        name = self.request.query_params.get("name", None)
        if name is not None:
            queryset = queryset.filter(name=name)
        type_ = self.request.query_params.get("type", None)
        if type_ is not None:
            print(type_)
            queryset = queryset.filter(type=type_)
        return queryset

    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            customer = serializer.save()
            serializer_response = CustomerSerializer(customer)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
# @api_view(["GET", "POST"])
# def products(request):
#     if request.method == "GET":
#         queryset = Product.objects.all()

#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             customer = serializer.save()
#             serializer_response = CustomerSerializer(customer)
#             return Response(serializer_response.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerCreateView(CreateView):
    success_url = "buy_succes"
    template_name = "customer_form.html"
    model = Customer
    fields = ["name", "telephone", "email"]

    def form_valid(self, form):
        form.instance.product = Product.objects.get(slug=self.kwargs["slug"])
        return super().form_valid(form)


def main(request):
    return render(request, "home.html")
