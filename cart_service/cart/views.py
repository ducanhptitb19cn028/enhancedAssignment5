from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.views import View
from .models import CartItem

class CartDetailView(View):
    def get(self, request, *args, **kwargs):
        cart_items = CartItem.objects.all()
        books = []
        for cart_item in cart_items:
            response = requests.get(f'http://localhost:8001/api/book/books/{cart_item.book_id}/')
            book_data = response.json()
            book_data['quantity'] = cart_item.quantity
            books.append(book_data)
        context = {
            'books': books
        }
        return render(request, 'cart_detail.html', context)
