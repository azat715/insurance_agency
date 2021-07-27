from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.edit import CreateView

from core.models import Product, Customer

from .serializers import ProductSerializer

# Create your views here.
@api_view()
def products(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)


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
