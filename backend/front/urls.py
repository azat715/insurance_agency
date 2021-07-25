from django.urls import path
from django.views.generic import TemplateView

from front.views import main, ProductsList, CustomerCreateView

app_name = "front"

urlpatterns = [
    path("", main, name="product-front"),
    path("product/<slug:slug>/buy/", CustomerCreateView.as_view(), name="product_buy"),
    path(
        "product/<slug:slug>/buy/buy_succes",
        TemplateView.as_view(template_name="buy_succes.html"),
        name="buy_succes",
    ),
    path("api/products/", ProductsList.as_view(), name="product-list"),
]
