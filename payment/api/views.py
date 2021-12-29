from rest_framework.response import Response

from .models import PaymentTransaction
from .serializers import PaymentTransactionSerializer
from rest_framework import generics, status

from .service import PaymentTransactionService


class PaymentTransactView(generics.CreateAPIView):
    queryset = PaymentTransaction()
    serializer_class = PaymentTransactionSerializer
    service = PaymentTransactionService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            tx = self.service.send(
                _from=serializer.validated_data.get('_from'),
                to=serializer.validated_data.get('to'),
                price=serializer.validated_data.get('price'),
                private_key=serializer.validated_data.get('private_key')
            )
            data = dict(serializer.validated_data)
            data['transaction'] = tx
            serializer.update(serializer, data)
            headers = self.get_success_headers(serializer.data)
            return Response({"transaction": tx}, status=status.HTTP_201_CREATED,
                            headers=headers)
        except Exception as e:
            raise e
