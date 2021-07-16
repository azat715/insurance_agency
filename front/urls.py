from django.urls import path

from front.views import main, products

app_name = "front"

urlpatterns = [
    path("", main, name="product-front"),
    path("api/products/", products, name="product-list"),
]
