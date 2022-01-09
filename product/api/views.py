from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics, status

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
            data = dict(serializer.validated_data)
            data['transaction'] = tx
            serializer.update(serializer, data)
            headers = self.get_success_headers(serializer.data)
            return Response({"transaction": tx}, status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            raise e
