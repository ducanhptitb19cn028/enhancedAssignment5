from django.urls import path
from .views import CartDetailView

app_name = 'cart_service'

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart_detail'),
]
