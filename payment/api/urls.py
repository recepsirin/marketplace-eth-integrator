from django.urls import path, include
from .views import PaymentTransactView

urlpatterns = [
    path('transact/', PaymentTransactView.as_view(), name='transact'),
]

urlpatterns = [
    path('payment/', include(urlpatterns)),
]