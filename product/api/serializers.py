from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'category', 'price',
                  'description']
        optional_fields = ['transaction', ]

    def update(self, instance, validated_data):
        instance.product_id = validated_data.get('product_id')
        instance.product_name = validated_data.get('product_name')
        instance.category = validated_data.get('category')
        instance.price = validated_data.get('price')
        instance.transaction = validated_data.get('transaction')
        instance.save()
