from django.db import models
import requests

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    category = models.CharField(max_length=255)

    @staticmethod
    def get_book(book_id):
        response = requests.get(f'http://127.0.0.1:8001/api/book/books/{book_id}/')
        if response.status_code == 200:
            book_data = response.json()
            book = Book(
                title=book_data['title'],
                author=book_data['author'],
                publisher=book_data['publisher'],
                category=book_data['category'],
            )
            return book
        else:
            return None
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name


class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
