from rest_framework import serializers
from .models import PaymentTransaction


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = ['to', '_from', 'price', 'private_key']
        optional_fields = ['transaction', ]

    def update(self, instance, validated_data):
        instance.to = validated_data.get('to')
        instance._from = validated_data.get('_from')
        instance.price = validated_data.get('price')
        instance.private_key = validated_data.get('private_key')
        instance.transaction = validated_data.get('transaction')
        instance.save()
