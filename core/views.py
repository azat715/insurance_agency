from django.db import models
from django.urls import path, reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from core.forms import NewUserForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from core.models import Seller, Product

# Create your views here.
def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("core:account")
        else:
            print(form.errors)
    else:
        form = NewUserForm()
    return render(
        request=request, template_name="register.html", context={"form": form}
    )


class SellerDetail(DetailView, LoginRequiredMixin):
    template_name = "seller_detail.html"
    model = Seller

    def get_object(self):
        return get_object_or_404(Seller, pk=self.request.user.id)


class ProductList(ListView, LoginRequiredMixin):
    template_name = "product_list.html"
    model = Product

    def get_queryset(self):
        return super().get_queryset().filter(seller__id=self.request.user.id)


class ProductCreateView(CreateView, LoginRequiredMixin):
    template_name = "product_form.html"
    model = Product
    fields = [
        "name",
        "description",
        "type",
        "price",
        "percentage_rate",
        "insurance_period",
    ]

    def get_success_url(self):
        return reverse("core:product-list", current_app="core")

    def form_valid(self, form):
        form.instance.seller_id = self.request.user.id
        return super().form_valid(form)


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    template_name = "product_form.html"
    model = Product
    fields = [
        "name",
        "description",
        "type",
        "price",
        "percentage_rate",
        "insurance_period",
    ]

    def get_success_url(self):
        return reverse("core:product-list", current_app="core")
