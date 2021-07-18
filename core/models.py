import datetime
from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta
from django.core.validators import MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Seller(User):
    class Meta:
        proxy = True


class Product(models.Model):
    AUTO_INSURANCE = "AUTO"
    HOME_INSURANCE = "HOME"
    LIFE_INSURANCE = "LIFE"
    PRODUCT_TYPES = [
        (AUTO_INSURANCE, "Auto insurance"),
        (HOME_INSURANCE, "Home insurance"),
        (LIFE_INSURANCE, "Life insurance"),
    ]

    THREE_MONTHS = timedelta(days=90)
    SIX_MONTHS = timedelta(days=180)
    TWELVE_MONTHS = timedelta(days=365)
    DURATION_INSURANCE = [
        (THREE_MONTHS, "Три месяца"),
        (TWELVE_MONTHS, "Шесть месяцев"),
        (TWELVE_MONTHS, "Двенадцать месяцев"),
    ]

    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    type = models.CharField(max_length=4, choices=PRODUCT_TYPES)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    percentage_rate = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(100)]
    )
    insurance_period = models.DurationField(choices=DURATION_INSURANCE)
    published = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    slug = models.SlugField(null=False, unique=True)
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="products"
    )

    def buy_url(self):
        return reverse(
            "front:product_buy", kwargs={"slug": self.slug}, current_app="front"
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Customer(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="customers"
    )
    name = models.CharField(max_length=20)
    telephone = models.CharField(max_length=17, blank=True)
    email = models.EmailField()
