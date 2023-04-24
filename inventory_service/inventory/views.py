import requests
from rest_framework import generics, permissions
from .models import Product, Stock, Book
from .serializers import ProductSerializer, StockSerializer

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

class StockListView(generics.ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Stock.objects.all()
        book_id = self.request.query_params.get('book_id', None)
        if book_id is not None:
            queryset = queryset.filter(book__id=book_id)
        return queryset


class StockDetailView(generics.RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'book': Book.get_book(self.get_object().book_id),
        })
        return context
