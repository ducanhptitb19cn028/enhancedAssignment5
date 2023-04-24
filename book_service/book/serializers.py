from rest_framework import serializers
from .models import Author, Publisher, Category, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'email']


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'category', 'price', 'description', 'image_url']
