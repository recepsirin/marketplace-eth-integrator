from django.db import models


class PaymentTransaction(models.Model):
    to = models.CharField(max_length=128)
    _from = models.CharField(max_length=128)
    price = models.IntegerField()
    private_key = models.CharField(max_length=256)
    transaction = models.CharField(max_length=8192)
