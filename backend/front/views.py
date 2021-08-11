from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView

from core.models import Product, Customer
from core.redis_client import RedisConfig, RedisClient

from .serializers import ProductSerializer

redis_config = RedisConfig.get_config()

# Create your views here.
@api_view()
def products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


class ProductDetail(DetailView):
    model = Product
    template_name = "product.html"

    def get(self, request, *args, **kwargs):
        r = RedisClient(redis_config)
        r.connect()
        r.counter(request.path)
        return super().get(request, *args, **kwargs)


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
