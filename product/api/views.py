from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics

from .service import SmartContractService


class ProductCreateView(generics.CreateAPIView, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    service = SmartContractService()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            tx = self.service.write_to_eth(
                product_id=serializer.validated_data.get('product_id'),
                product_name=serializer.validated_data.get('product_name'),
                category=serializer.validated_data.get('category'),
                price=serializer.validated_data.get('price'),
                description=serializer.validated_data.get('description')
            )
            serializer.update("transaction", tx)
        except Exception as e:
            raise e
        return self.create(request, *args, **kwargs)
