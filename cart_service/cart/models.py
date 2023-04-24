from django.db import models

# Create your models here.

class CartItem(models.Model):
    book_id = models.IntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Book ID: {self.book_id}, Quantity: {self.quantity}"
