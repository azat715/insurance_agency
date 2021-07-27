from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "core"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.register_request, name="register"),
    path("account/", views.SellerDetail.as_view(), name="account"),
    path("account/products/", views.ProductList.as_view(), name="product-list"),
    path("account/product/add/", views.ProductCreateView.as_view(), name="product-add"),
    path(
        "account/products/<slug:slug>/sellers/",
        views.CustomerList.as_view(),
        name="сustomer-list",
    ),
]
