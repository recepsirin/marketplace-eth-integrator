from django.db import models


class ContractTransaction(models.Model):
    tx = models.CharField(verbose_name="transaction", max_length=8192)


class Product(models.Model):
    product_id = models.CharField(verbose_name="productId", max_length=60)
    product_name = models.CharField(verbose_name="productName", max_length=120)
    category = models.CharField(verbose_name="category", max_length=120)
    price = models.IntegerField(verbose_name="price")
    description = models.CharField(verbose_name="description", max_length=240)
    transaction = models.OneToOneField(
        ContractTransaction,
        on_delete=models.CASCADE,
        primary_key=True,
    )
