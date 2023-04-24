from rest_framework import serializers

from .models import Product, Stock, Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class StockSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()

    class Meta:
        model = Stock
        fields = ['id', 'book', 'quantity']

    def get_book(self, obj):
        book_data = Book.get_book(obj.book_id)
        if book_data:
            return {
                'id': obj.book_id,
                'title': book_data.title,
                'author': book_data.author,
                'publisher': book_data.publisher,
                'category': book_data.category,
            }
        else:
            return None
